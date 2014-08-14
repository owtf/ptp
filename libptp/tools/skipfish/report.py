"""

:synopsis: Specialized Report class for Skipfish.

.. moduleauthor:: Tao Sauvage

"""

import os

from libptp.exceptions import ReportNotFoundError
from libptp.report import AbstractReport
from libptp.tools.skipfish.parser import SkipfishJSParser


class SkipfishReport(AbstractReport):
    """Retrieve the information of a Skipfish report."""

    __tool__ = 'skipfish'
    __parsers__ = [SkipfishJSParser]

    _reportfile = 'samples.js'
    _metadatafile = 'summary.js'

    def __init__(self):
        """Initialize SkipfishReport."""
        AbstractReport.__init__(self)

    @classmethod
    def is_mine(cls, pathname):
        """Check if it is a Skipfish report and if it can handle it.

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
        return AbstractReport._is_parser(
            cls.__parsers__,
            metadatafile,
            reportfile)

    def parse(self, pathname):
        """Parse a Skipfish report.

        :param str pathname: Path to the report directory.
        :raises: :class:`ReportNotFoundError` -- if the report was not found.

        :return: List of dicts where each one represents a discovery from the
            report.
        :rtype: :class:`list`

        """
        if not os.path.isdir(pathname):
            raise ReportNotFoundError(
                'A directory to the report MUST be specified.')
        # Find metadata file.
        metadatafile = self._recursive_find(pathname, self._metadatafile)
        if not metadatafile:
            raise ReportNotFoundError('The metadata file was not found.')
        self.metadatafile = metadatafile[0]
        # Find report file.
        reportfile = self._recursive_find(pathname, self._reportfile)
        if not reportfile:
            raise ReportNotFoundError('The report file was not found.')
        self.reportfile = reportfile[0]
        # Find the corresponding parser.
        self._init_parser(self.metadatafile, self.reportfile)
        # Parser everything.
        self.metadata = self.parser.parse_metadata()
        self.vulns = self.parser.parse_report()
        return self.vulns
