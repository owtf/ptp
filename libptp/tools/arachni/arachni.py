from __future__ import print_function

from lxml import etree

from libptp import constants
from libptp.info import Info
from libptp.report import AbstractReport


class ArachniReport(AbstractReport):
    """Retrieve the information of a skipfish report."""

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
        self.vulns = []

    def parse(self, path_to_report=None, filename=None):
        """Parse an arachni resport."""
        # Reconstruct the path to the report if any.
        self.directory = ''
        if not path_to_report is None:
            self.directory = path_to_report
        if not filename is None:
            self.directory = os.path.join(self.directory, filename)

        # Parse the XML report thanks to lxml.
        self.root = etree.parse(self.directory).getroot()
        # Parse specific stuff.
        self.parse_xml_metadata()
        self.parse_xml_report()
        # TODO: Return something like an unified version of the report.
        return self.vulns

    def _check_version(self, metadata):
        """Checks the version from the metadata to the supported one."""
        if metadata['version'] in self.__version__:
            return True
        return False

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
        if self._check_version(metadata):
            self.metadata = metadata
        else:
            # TODO: Implement custom exception
            raise ValueError(
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
