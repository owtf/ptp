"""

:synopsis: Specialized Parser classes for Skipfish.

.. moduleauthor:: Tao Sauvage

"""

import re
import ast

from libptp.exceptions import NotSupportedVersionError, ReportNotFoundError
from libptp.parser import AbstractParser


class SkipfishJSParser(AbstractParser):
    """Skipfish JS specialized parser."""

    #: :class:`str` -- Name of the tool.
    __tool__ = 'skipfish'
    #: :class:`str` -- Format of Skipfish reports it supports.
    __format__ = 'js'
    #: :class:`list` -- Skipfish versions it supports.
    __version__ = ['2.10b']

    def __init__(self, metadatafile, reportfile):
        """Initialize ArachniXMLParser.

        :param str metadatafile: full path to the metadata file.
        :param str reportfile: full path to the report file.

        """
        self.metadata_stream, self.report_stream = self.handle_file(
            metadatafile, reportfile)
        self.re_metadata = re.compile(
            r"var\s+([a-zA-Z_0-9]+)\s+=\s+'{0,1}([^;']*)'{0,1};")
        self.re_report = re.compile(
            r"var\s+([a-zA-Z_0-9]+)\s+=\s+([^;]*);")

    @classmethod
    def handle_file(cls, metadatafile, reportfile):
        """Create handlers on the Skipfish report files.

        :param str metadatafile: Path to the metadata file.
        :param str reportfile: Path to the report file.
        :raises ValueError: if the files have not the right extension.
        :raises OSError: if an error occurs when reading the files.
        :raises IOError: if an error occurs when reading the files.

        :return: Both metadata and report files' contents.
        :rtype: :class:`tuple`

        """
        if (not metadatafile.endswith(cls.__format__) or
                not reportfile.endswith(cls.__format__)) :
            raise ValueError(
                "This parser only supports '%s' files" % cls.__format__)
        with open(metadatafile, 'r') as f:
            metadata_stream = f.read()
        with open(reportfile, 'r') as f:
            report_stream = f.read()
        return (metadata_stream, report_stream)

    @classmethod
    def is_mine(cls, metadatafile, reportfile):
        """Check if it is a supported Skipfish report.

        :param str metadatafile: Path to the metadata file.
        :param str reportfile: Path to the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            metadata_stream, report_stream = cls.handle_file(
                metadatafile,
                reportfile)
        except (OSError, IOError, ValueError):
            return False
        return True

    def parse_metadata(self):
        """Retrieve the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support
            this version of the report.

        :return: Dictionary containing the metadatas.
        :rtype: :class:`dict`

        .. note::

            In skipfish the metadata are saved into the summary.js file as
            follow:

            .. code-block:: js

                var sf_version = version<string>;
                var scan_date  = date<'Ddd Mmm d hh:mm:ss yyyy'>;
                var scan_seed  = scan seed<integer>
                var scan_ms    = elapsed time in ms<integer>;

        """
        re_result = self.re_metadata.findall(self.metadata_stream)
        metadata = dict({el[0]: el[1] for el in re_result})
        # Check if the version if the good one
        if self.check_version(metadata, key='sf_version'):
            return metadata
        else:
            raise NotSupportedVersionError(
                'PTP does NOT support this version of Skipfish.')

    def parse_report(self, scale):
        """Retrieve the results from the report.

        :param dict scale: Unified scale between Skipfish and PTP.
        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        :raises: :class:`ReportNotFoundError` -- if the report file was not
            found.

        .. note::

            Example of retrieved data after conversion (i.e. `raw_report`)
            using the module :mod:`ast`:

            .. code-block:: js

                [{ 'severity': 3, 'type': 40402, 'samples': [
                    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/0' },
                    { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/1' },
                    { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/2' } ]
                },]

        """
        REPORT_VAR_NAME = 'issue_samples'
        re_result = self.re_report.findall(self.report_stream)
        report = dict({el[0]: el[1] for el in re_result})
        if not REPORT_VAR_NAME in report:
            raise ReportNotFoundError(
                'PTP did NOT find issue_samples variable. Is this the '
                'right file?')
        # We now have a raw version of the Skipfish report as a list of
        # dict.
        self.vulns = [
            {'ranking': scale[vuln['severity']]}
            for vuln in ast.literal_eval(report[REPORT_VAR_NAME])]
        return self.vulns
