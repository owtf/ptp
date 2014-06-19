from __future__ import print_function

import os

from lxml import etree
from lxml.etree import LxmlError

from libptp.exceptions import NotSupportedVersionError
from libptp import constants
from libptp.report import AbstractReport
from libptp.tools.arachni.parser import ArachniXMLParser


class ArachniReport(AbstractReport):
    """Retrieve the information of an arachni report."""

    __tool__ = 'arachni'
    __parsers__ = {ArachniXMLParser: '0.4.6'}

    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    INFO = 'Informational'

    # Convert the Arachni's ranking scale to an unified one.
    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    def __init__(self, *args, **kwargs):
        AbstractReport.__init__(self, *args, **kwargs)

    @classmethod
    def is_mine(cls, pathname, filename='*.xml'):
        """Check if it is a Arachni report and if I can handle it.

        Return True if it is mine, False otherwise.

        """
        fullpath = cls._recursive_find(pathname, filename)
        if not fullpath:
            return False
        fullpath = fullpath[0]  # Only keep the first file.
        return AbstractReport._is_parser(fullpath, cls.__parsers__)

    def parse(self, pathname=None, filename='*.xml'):
        """Parse an arachni resport."""
        # Reconstruct the path to the report if any.
        self.fullpath = self._recursive_find(pathname, filename)[0]
        # Find the corresponding parser.
        self._init_parser(self.fullpath)
        # Parse specific stuff.
        self.metadata = self.parser.parse_metadata()
        self.vulns = self.parser.parse_report(self.RANKING_SCALE)
        # TODO: Return something like an unified version of the report.
        return self.vulns
