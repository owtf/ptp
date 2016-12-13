"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the tool Skipfish.

.. moduleauthor:: Tao Sauvage

"""

import re
import os
import ast
import js2py

from ptp.libptp import constants
from ptp.libptp.exceptions import NotSupportedVersionError, ReportNotFoundError
from ptp.libptp.parser import AbstractParser


class SkipfishJSParser(AbstractParser):
    """Skipfish JS specialized parser."""

    __tool__ = 'skipfish'
    __format__ = 'js'
    __version__ = r'2\.10b'

    HIGH = 4
    MEDIUM = 3
    LOW = 2
    WARNINGS = 1
    INFO = 0

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        WARNINGS: constants.INFO,
        INFO: constants.INFO}

    _reportfile = 'samples.js'
    _metadatafile = 'summary.js'
    dirname = ''

    def __init__(self, pathname, http_parse=False):
        """Initialize ArachniXMLParser.

        :param str pathname: Path to the report directory.

        """
        AbstractParser.__http_parse__ = http_parse
        metadatafile = self._recursive_find(pathname, self._metadatafile)
        if metadatafile:
            metadatafile = metadatafile[0]
        reportfile = self._recursive_find(pathname, self._reportfile)
        if reportfile:
            self.dirname = os.walk(pathname).next()[0]
            reportfile = reportfile[0]
        self.metadata_stream, self.report_stream = self.handle_file(metadatafile, reportfile)
        self.re_var_pattern = re.compile(r"var\s+(?P<variables>[a-zA-Z_0-9]+)\s+(?==)")
        self.re_metadata = re.compile(r"var\s+([a-zA-Z_0-9]+)\s+=\s+'{0,1}([^;']*)'{0,1};")
        self._re_reponse_status_code = re.compile(r"^HTTP.*?\/\d\.\d (\d+) .")

    @classmethod
    def handle_file(cls, metadatafile, reportfile):
        """Process the two report files of the Skipfish report.

        :param str metadatafile: Path to the metadata file.
        :param str reportfile: Path to the report file.
        :raises TypeError: if the files have not the right extension.
        :raises OSError: if an error occurs when reading the files.
        :raises IOError: if an error occurs when reading the files.

        :return: Both metadata and report files' contents.
        :rtype: :class:`tuple`

        """
        if not metadatafile.endswith(cls.__format__) or not reportfile.endswith(cls.__format__):
            raise TypeError("This parser only supports '%s' files" % cls.__format__)
        with open(metadatafile, 'r') as f:
            metadata_stream = f.read()
        with open(reportfile, 'r') as f:
            report_stream = f.read()
        return (metadata_stream, report_stream)

    @classmethod
    def is_mine(cls, pathname, http_parse=False):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.

        :raises IOError: when the report file cannot be found.
        :raises OSError: when the report file cannot be found.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        metadatafile = cls._recursive_find(pathname, cls._metadatafile)
        if not metadatafile:
            return False
        metadatafile = metadatafile[0]
        reportfile = cls._recursive_find(pathname, cls._reportfile)
        if not reportfile:
            return False
        reportfile = reportfile[0]
        try:
            metadata_stream, report_stream = cls.handle_file(metadatafile, reportfile)
        except TypeError:
            return False
        return True

    def parse_metadata(self):
        """Retrieve the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support this version of the report.

        :return: Dictionary containing the metadatas.
        :rtype: :class:`dict`

        .. note::

            In skipfish the metadata are saved into the summary.js file as follow:

            .. code-block:: js

                var sf_version = version<string>;
                var scan_date  = date<'Ddd Mmm d hh:mm:ss yyyy'>;
                var scan_seed  = scan seed<integer>
                var scan_ms    = elapsed time in ms<integer>;

        """
        re_result = self.re_metadata.findall(self.metadata_stream)
        metadata = dict({el[0]: el[1] for el in re_result})
        # Check if the version if the good one.
        if self.check_version(metadata, key='sf_version'):
            return metadata
        else:
            raise NotSupportedVersionError('PTP does NOT support this version of Skipfish.')

    def get_data(self, dir_list):
        """ Retrieve list of directories found in samples.js file. From all the directories, it reads request.dat
        and response.dat file and return a list of dict resquests and responses.

        :raises: IOError -- specifying in which directory it doesn't find request.dat/response.dat file and
        default its value to NOT_FOUND
        """
        data = []
        for dirs in dir_list:
            try:
                with open(dirs['dir']+'/request.dat', 'r') as req_data:
                    request = req_data.read()
            except IOError:
                print("request.dat file not found in "+dirs['dir']+" defaulting it NOT_FOUND")
                request = "NOT_FOUND"
            try:
                with open(dirs['dir']+'/response.dat', 'r') as res_data:
                    response = res_data.read()
                    response_status_code = self._re_reponse_status_code.findall(response)[0]
                    response_header, response_body = response.split('\n\n', 1)
            except IOError:
                print("response.dat file not found in "+dirs['dir']+" defaulting it NOT_FOUND")
                response_body = response_header = response_status_code = "NOT_FOUND"
            data.append({
                'request':request,
                'response_status_code': response_status_code,
                'response_headers': response_header,
                'response_body': response_body
            })
        return data

    def parse_report(self):
        """Retrieve the results from the report.

        :raises: :class:`ReportNotFoundError` -- if the report file was not found.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        .. note::

            Example of retrieved data after conversion (i.e. `raw_report`) using the module :mod:`ast`:

            .. code-block:: js

                [{ 'severity': 3, 'type': 40402, 'samples': [
                    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/0' },
                    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/1' },
                    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/2' } ]
                },]

        """
        REPORT_VAR_NAME = 'issue_samples'
        variables = self.re_var_pattern.findall(self.report_stream)
        split_data = self.report_stream.split(";")
        js_data = [data for data in split_data if data is not None]
        py_data = []
        format_data = {} # Final python dict after converting js to py
        dirs = [] # List of directories of all urls
        # Converting js to py to make it simple to process
        for data in js_data:
            temp_data = js2py.eval_js(data)
            if temp_data is not None:
                py_data.append(temp_data)

        # Mapping variable to its content
        for i in range(len(py_data)):
            format_data[variables[i]] = py_data[i]

        if REPORT_VAR_NAME not in variables:
            raise ReportNotFoundError('PTP did NOT find issue_samples variable. Is this the correct file?')
        # We now have a raw version of the Skipfish report as a list of dict.
        self.vulns = [
            {'ranking': self.RANKING_SCALE[vuln['severity']]}
            for vuln in format_data[REPORT_VAR_NAME]]
        if self.__http_parse__:
            for var in variables:
                for item in format_data[var]:
                    for sample in item['samples']:
                        dirs.append({'url':sample['url'], 'dir':self.dirname+'/'+sample['dir']})
            self.vulns.append({'transactions': self.get_data(dirs)})
        return self.vulns
