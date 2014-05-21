from __future__ import print_function

import os
from lxml import etree

from libptp import constants
from libptp.info import Info
from libptp.report import AbstractReport


class WapitiReport(AbstractReport):
    """Retrieve the information of an wapiti report."""

    __version__ = ['2.3.0']

    def __init__(self, *args, **kwargs):
        AbstractReport.__init__(self, *args, **kwargs)
        self.vulns = []

    def parse(self, path_to_report=None, filename=None):
        """Parse an Wapiti resport."""
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

    def parse_xml_metadata(self):
        """Retrieve the metadata of the report.

        #TODO: Complete the docstring.

        """
        # Find the metadata of Wapiti.
        raw_metadata = self.root.find('.//report_infos')
        # Reconstruct the metadata
        metadata = {el.get('name'): el.text for el in raw_metadata}
        # Only keep the version number
        metadata['generatorVersion'] = metadata['generatorVersion'].lstrip(
            'Wapiti ')
        if self.check_version(metadata, key='generatorVersion'):
            self.metadata = metadata
        else:
            # TODO: Implement custom exception
            raise ValueError(
                'PTP does NOT support this version of Wapiti.')

    def parse_xml_report(self):
        """Retrieve the results from the report.

        Retrieve the following attributes:
            + None

        #TODO: Complete the docstring.

        """
        vulns = self.root.find('.//vulnerabilities')
        for vuln in vulns.findall('.//vulnerability'):
            #info = Info(
            #    # Convert the severity of the issue thanks to an unified
            #    # ranking scale.
            #    ranking=self.RANKING_SCALE[vuln.find('.//severity').text]
            #    )
            #self.vulns.append(info)
            pass
