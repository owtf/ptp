"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the tool Wapiti.

.. moduleauthor:: Tao Sauvage

"""

import re

from lxml.etree import XMLSyntaxError

from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.libptp.constants import UNKNOWN
from ptp.libptp.parser import XMLParser
from ptp.tools.wapiti.signatures import SIGNATURES


class WapitiXMLParser(XMLParser):
    """Wapiti XML specialized parser."""

    __tool__ = 'wapiti'
    __format__ = 'xml'
    __version__ = r'^\D*(2\.3(\.[0-9]+)?)$'

    @classmethod
    def is_mine(cls, pathname, filename='*.xml', light=True, first=True):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool light: `True` to only parse the ranking of the findings from the report.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        :raises IOError: when the report file cannot be found.
        :raises OSError: when the report file cannot be found.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename, first=first)
        except (TypeError, XMLSyntaxError):
            return False
        raw_metadata = stream.find('.//report_infos')
        if raw_metadata is None:
            return False
        metadata = {el.get('name'): el.text for el in raw_metadata}
        if metadata.get('generatorName', '').lower() != cls.__tool__:
            return False
        if not re.match(cls.__version__, metadata.get('generatorVersion', '')):
            return False
        return True

    def parse_metadata(self):
        """Parse the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support the version of this report.

        :return: The metadata of the report.
        :rtype: dict

        """
        # Find the metadata of Wapiti.
        raw_metadata = self.stream.find('.//report_infos')
        # Reconstruct the metadata
        metadata = {el.get('name'): el.text for el in raw_metadata}
        # Only keep the version number
        metadata['generatorVersion'] = metadata['generatorVersion'].lstrip('Wapiti ')
        if not self.check_version(metadata, key='generatorVersion'):
            raise NotSupportedVersionError('PTP does NOT support this version of Wapiti.')
        self.metadata = metadata
        return metadata

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        section_vuln = self.stream.find('.//vulnerabilities')
        if section_vuln is None:
            return []
        vulns = []
        for category in section_vuln.findall('.//vulnerability'):
            entries = category.find('.//entries')
            if not len(entries):
                pass
            # Ensure that there are 'entry' sub-sections that represent the
            # actual discoveries/vulnerabilities.
            if len(entries.findall('.//entry')) and category.get('name') in SIGNATURES:
                vulns.append({
                    'name': category.get('name'),
                    'ranking': SIGNATURES.get(category.get('name'), UNKNOWN),
                    'description': category.find('.//description').text})
        self.vulns = vulns
        return vulns


class Wapiti221XMLParser(XMLParser):
    """Wapiti XML specialized parser."""

    #: :class:`str` -- Name of the tool.
    __tool__ = 'wapiti'
    #: :class:`str` -- Format of Wapiti reports it supports.
    __format__ = 'xml'
    #: :class:`list` -- Wapiti versions it supports.
    __version__ = r'2\.2(\.[0-9]+)?'

    @classmethod
    def is_mine(cls, pathname, filename='*.xml', light=True, first=True):
        """Check if it is a supported Wapiti report.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool light: `True` to only parse the ranking of the findings from the report.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename, first=first)
        except (IOError, XMLSyntaxError):
            return False
        raw_metadata = stream.find('.//generatedBy')
        if raw_metadata is None:
            return False
        metadata = raw_metadata.get('id')
        if not re.findall(cls.__version__, metadata, re.IGNORECASE):
            return False
        return True

    def parse_metadata(self):
        """Parse the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support the version of this report.

        :return: The metadata of the report.
        :rtype: dict

        """
        # Find the metadata of Wapiti.
        raw_metadata = self.stream.find('.//generatedBy').get('id')
        metadata = {}
        # Only keep the version number
        metadata['version'] = raw_metadata
        if not self.check_version(metadata):
            raise NotSupportedVersionError('PTP does NOT support this version of Wapiti.')
        self.metadata = metadata
        return self.metadata

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        section_vuln = self.stream.find('.//bugTypeList')
        vulns = []
        for category in section_vuln.findall('.//bugType'):
            entries = category.find('.//bugList')
            if not len(entries):
                pass
            # Ensure that there are 'entry' sub-sections that represent the actual discoveries/vulnerabilities.
            if len(entries.findall('.//bug')) and category.get('name') in SIGNATURES:
                vulns.append({
                    'name': category.get('name'),
                    'ranking': SIGNATURES.get(category.get('name'), UNKNOWN),
                    'description': category.find('.//description').text})
        self.vulns = vulns
        return vulns
