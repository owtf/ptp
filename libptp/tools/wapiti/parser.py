"""

.. module:: parser
    :synopsis: Specialized Parser classes for Wapiti.

.. moduleauthor:: Tao Sauvage

"""

from libptp.exceptions import NotSupportedVersionError
from libptp.parser import XMLParser
from libptp.tools.wapiti.signatures import SIGNATURES


class WapitiXMLParser(XMLParser):

    #: :class:`str` -- Name of the tool.
    __tool__ = 'wapiti'
    #: :class:`str` -- Format of Wapiti reports it supports.
    __format__ = 'xml'
    #: :class:`list` -- Wapiti versions it supports.
    __version__ = ['2.3.0']

    def __init__(self, pathname):
        XMLParser.__init__(self, pathname)

    @classmethod
    def is_mine(cls, pathname):
        """Check if it is a supported Wapiti report.

        :param str pathname: Path to the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        stream = cls.handle_file(pathname)
        raw_metadata = stream.find('.//report_infos')
        if raw_metadata is None:
            return False
        metadata = {el.get('name'): el.text for el in raw_metadata}
        if not metadata:
            return False
        if metadata['generatorName'].lower() != cls.__tool__:
            return False
        return True

    def parse_metadata(self):
        """Parse the metadatas of the report.

        :return: The metadatas of the report.
        :rtype: dict

        :raises: :class:`NotSupportedVersionError` -- if it does not support
            the version of this report.

        """
        # Find the metadata of Wapiti.
        raw_metadata = self.stream.find('.//report_infos')
        # Reconstruct the metadata
        metadata = {el.get('name'): el.text for el in raw_metadata}
        # Only keep the version number
        metadata['generatorVersion'] = metadata['generatorVersion'].lstrip(
            'Wapiti ')
        if self.check_version(metadata, key='generatorVersion'):
            self.metadata = metadata
        else:
            raise NotSupportedVersionError(
                'PTP does NOT support this version of ' + self.__tool__ + '.')

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a vuln.
        :rtype: :class:`list`

        """
        vulns = self.stream.find('.//vulnerabilities')
        return [{
            'name': vuln.get('name'),
            'ranking': SIGNATURES.get(vuln.get('name')),
            'description':vuln.find('.//description')}
            for vuln in vulns.findall('.//vulnerability')
            if vuln.get('name') in SIGNATURES]
