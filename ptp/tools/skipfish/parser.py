"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the
    tool Skipfish.

.. moduleauthor:: Tao Sauvage

"""

import re
import ast

from ptp.libptp import constants
from ptp.libptp.exceptions import NotSupportedVersionError, ReportNotFoundError
from ptp.libptp.parser import AbstractParser


class SkipfishJSParser(AbstractParser):
    """Skipfish JS specialized parser."""

    __tool__ = 'skipfish'
    __format__ = 'js'
    __version__ = ['2.10b']

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

    def __init__(self, pathname):
        """Initialize ArachniXMLParser.

        :param str pathname: Path to the report directory.

        """
        metadatafile = self._recursive_find(pathname, self._metadatafile)
        if not metadatafile:
            return False
        metadatafile = metadatafile[0]
        reportfile = self._recursive_find(pathname, self._reportfile)
        if not reportfile:
            return False
        reportfile = reportfile[0]
        self.metadata_stream, self.report_stream = self.handle_file(
            metadatafile, reportfile)
        self.re_metadata = re.compile(
            r"var\s+([a-zA-Z_0-9]+)\s+=\s+'{0,1}([^;']*)'{0,1};")
        self.re_report = re.compile(
            r"var\s+([a-zA-Z_0-9]+)\s+=\s+([^;]*);")

    @classmethod
    def handle_file(cls, metadatafile, reportfile):
        """Process the two report files of the Skipfish report.

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
    def is_mine(cls, pathname):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.

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

    def parse_report(self):
        """Retrieve the results from the report.

        :raises: :class:`ReportNotFoundError` -- if the report file was not
            found.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

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
            {'ranking': self.RANKING_SCALE[vuln['severity']]}
            for vuln in ast.literal_eval(report[REPORT_VAR_NAME])]
        return self.vulns
