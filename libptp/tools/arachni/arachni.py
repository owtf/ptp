from __future__ import print_function

import os

from lxml import etree
from lxml.etree import LxmlError

from libptp.exceptions import NotSupportedVersionError
from libptp import constants
from libptp.info import Info
from libptp.report import AbstractReport


class ArachniReport(AbstractReport):
    """Retrieve the information of an arachni report."""

    __tool__ = 'arachni'
    __version__ = ['0.4.6']

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
    def is_mine(cls, pathname, filename=None):
        """Check if it is a Arachni report and if I can handle it.

        Return True if it is mine, False otherwise.

        """
        fullpath = cls._get_fullpath(pathname, filename=filename)
        if not fullpath:
            return False
        if not fullpath.endswith('.xml'):
            return False
        try:
            root = etree.parse(fullpath).getroot()
        except LxmlError:  # Not a valid XML file.
            return False
        return cls._is_arachni(root)

    @classmethod
    def _is_arachni(cls, xml_report):
        """Check if the xml_report comes from Arachni.

        Returns True if it is from Arachni, False otherwise.

        """
        if not cls.__tool__ in xml_report.tag:
            return False
        return True

    def parse(self, pathname=None, filename=None):
        """Parse an arachni resport."""
        # Reconstruct the path to the report if any.
        self.directory = ''
        if not pathname is None:
            self.directory = pathname
        if not filename is None:
            self.directory = os.path.join(self.directory, filename)

        # Parse the XML report thanks to lxml.
        self.root = etree.parse(self.directory).getroot()
        # Parse specific stuff.
        self.parse_xml_metadata()
        self.parse_xml_report()
        # TODO: Return something like an unified version of the report.
        return self.vulns

    def parse_xml_metadata(self):
        """Retrieve the metadata of the report.

        #TODO: Complete the docstring.

        """
        # Find the version of Arachni.
        version = self.root.find('.//version')
        # Reconstruct the metadata
        # TODO: Retrieve the other metadata likes the date, etc.
        metadata = {
            version.tag: version.text,}
        if self.check_version(metadata):
            self.metadata = metadata
        else:
            raise NotSupportedVersionError(
                'PTP does NOT support this version of Arachni.')

    def parse_xml_report(self):
        """Retrieve the results from the report.

        Retrieve the following attributes:
            + severity

        #TODO: Complete the docstring.

        """
        vulns = self.root.find('.//issues')
        for vuln in vulns.findall('.//issue'):
            info = Info(
                # Convert the severity of the issue thanks to an unified
                # ranking scale.
                ranking=self.RANKING_SCALE[vuln.find('.//severity').text]
                )
            self.vulns.append(info)
