from __future__ import print_function

import os

from lxml import etree
from lxml.etree import LxmlError

from libptp.exceptions import NotSupportedVersionError
from libptp import constants
from libptp.report import AbstractReport
from libptp.tools.wapiti.parser import WapitiXMLParser


class WapitiReport(AbstractReport):
    """Retrieve the information of an wapiti report."""

    __tool__ = 'wapiti'
    __parsers__ = {WapitiXMLParser: '2.3.0'}

    def __init__(self, *args, **kwargs):
        AbstractReport.__init__(self, *args, **kwargs)

    @classmethod
    def is_mine(cls, pathname, filename='*.xml'):
        """Check if it is a Wapiti report and if I can handle it.

        Return True if it is mine, False otherwise.

        """
        fullpath = cls._recursive_find(pathname, filename)
        if not fullpath:
            return False
        fullpath = fullpath[0]  # Only keep the first file.
        return AbstractReport._is_parser(fullpath, cls.__parsers__)

    def parse(self, pathname=None, filename='*.xml'):
        """Parse an Wapiti resport."""
        # Reconstruct the path to the report if any.
        self.fullpath = self._recursive_find(pathname, filename)[0]
        # Find the corresponding parser.
        self._init_parser(self.fullpath)
        # Parse specific stuff.
        self.metadata = self.parser.parse_metadata()
        self.vulns = self.parser.parse_report()
        # TODO: Return something like an unified version of the report.
        return self.vulns
