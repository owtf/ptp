import re

from libptp.exceptions import NotSupportedVersionError
from libptp.parser import XMLParser


class W3AFXMLParser(XMLParser):

    __tool__ = 'w3af'
    __format__ = 'xml'
    __version__ = ['1.6.0.2']

    def __init__(self, pathname):
        XMLParser.__init__(self, pathname)
        self.re_version = re.compile(r'Version: (\S*)\s')

    @classmethod
    def is_mine(cls, pathname):
        """Check if it is a supported report."""
        stream = cls.handle_file(pathname)
        if stream.find('.//w3af-version') is None:
            return False
        return True

    def parse_metadata(self):
        """Parse the metadatas of the report."""
        raw_metadata = self.stream.find('.//w3af-version').text
        # Find the version of w3af.
        version = self.re_version.findall(raw_metadata)
        if len(version) >= 1:  # In case we found several version numbers.
            version = version[0]
        # Reconstruct the metadata
        # TODO: Retrieve the other metadata likes the date, etc.
        metadata = {'version': version,}
        if self.check_version(metadata):
            self.metadata = metadata
        else:
            raise NotSupportedVersionError(
                'PTP does NOT support this version of ' + self.__tool__ + '.')

    def parse_report(self, scale):
        """Parse the report."""
        return [
            {'ranking': scale[vuln.get('severity')],}
            for vuln in self.stream.findall('.//vulnerability')]
