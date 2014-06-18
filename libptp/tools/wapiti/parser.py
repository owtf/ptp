from libptp.exceptions import NotSupportedVersionError
from libptp.info import Info
from libptp.parser import AbstractParser
from libptp.tools.wapiti.signatures import SIGNATURES


class WapitiXMLParser(AbstractParser):

    __tool__ = 'wapiti'
    __format__ = 'xml'
    __version__ = ['2.3.0']

    def __init__(self, *args, **kwargs):
        AbstractParser.__init__(self, *args, **kwargs)

    @classmethod
    def is_mine(cls, stream):
        """Check if it is a supported report."""
        raw_metadata = stream.find('.//report_infos')
        if raw_metadata is None:
            return False
        metadata = {el.get('name'): el.text for el in raw_metadata}
        if not metadata:
            return False
        if metadata['generatorName'].lower() != cls.__tool__:
            return False
        return True

    def parse_metadata(self, stream):
        """Parse the metadatas of the report."""
        # Find the metadata of Wapiti.
        raw_metadata = stream.find('.//report_infos')
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

    def parse_report(self, stream):
        """Parse the report."""
        vulns = stream.find('.//vulnerabilities')
        return [{
            'name': vuln.get('name'),
            'ranking': SIGNATURES.get(vuln.get('name')),
            'description':vuln.find('.//description')}
            for vuln in vulns.findall('.//vulnerability')]
