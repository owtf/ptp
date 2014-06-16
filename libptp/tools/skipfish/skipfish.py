from __future__ import print_function

import os

from libptp.exceptions import ReportNotFoundError, NotSupportedVersionError
from libptp import constants
from libptp.report import AbstractReport
from libptp.tools.skipfish.parser import SkipfishJSONParser


class SkipfishReport(AbstractReport):
    """Retrieve the information of a skipfish report."""

    __tool__ = 'skipfish'
    __parsers__ = {SkipfishJSONParser: '2.10b'}
    _reportfile = 'samples.js'
    _metadatafile = 'summary.js'

    HIGH = 4
    MEDIUM = 3
    LOW = 2
    WARNINGS = 1
    INFO = 0

    # Convert the Skipfish's ranking scale to an unified one.
    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        WARNINGS: constants.INFO,
        INFO: constants.INFO}

    def __init__(self, *args, **kwargs):
        AbstractReport.__init__(self, *args, **kwargs)

    @classmethod
    def is_mine(cls, pathname):
        """Check if it is a Skipfish report and if I can handle it.

        Return True if it is mine, False otherwise.

        """
        if not cls._recursive_find(pathname, cls._metadatafile):
            return False
        if not cls._recursive_find(pathname, cls._reportfile):
            return False
        # FIXME: Find a nice way to check for a correct parser.
        return AbstractReport._is_parser(None, cls.__parsers__)

    def parse(self, pathname=None):
        """Parse a skipfish report."""
        if (pathname is None or not os.path.isdir(pathname)):
            raise ReportNotFoundError(
                'A directory to the report MUST be specified.')
        # Find the corresponding parser.
        # FIXME: Find a nice way to check for a correct parser.
        self._init_parser(None)
        # Parse metadata.
        fullpath = self._recursive_find(pathname, self._metadatafile)
        if not fullpath:
            raise ReportNotFoundError('The metadata file is not found.')
        fullpath = fullpath[0]
        with open(fullpath, 'r') as f:
            self.metadata = self.parser.parse_metadata(f.read())
        # Parse report.
        fullpath = self._recursive_find(pathname, self._reportfile)
        if not fullpath:
            raise ReportNotFoundError('The report file is not found.')
        fullpath = fullpath[0]
        with open(fullpath, 'r') as f:
            self.vulns = self.parser.parse_report(f.read(), self.RANKING_SCALE)
        return self.vulns
