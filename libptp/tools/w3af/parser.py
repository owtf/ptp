import re

from libptp.exceptions import NotSupportedVersionError
from libptp.info import Info
from libptp.parser import AbstractParser


class W3AFXMLParser(AbstractParser):

    __tool__ = 'w3af'
    __format__ = 'xml'
    __version__ = ['1.6.0.2']

    def __init__(self, *args, **kwargs):
        AbstractParser.__init__(self, *args, **kwargs)
        self.re_version = re.compile(r'Version: (\S*)\s')

    @classmethod
    def is_mine(cls, stream):
        """Check if it is a supported report."""
        raw_metadata = stream.find('.//w3af-version')
        if raw_metadata is None:
            return False
        return True

    def parse_metadata(self, stream):
        """Parse the metadatas of the report."""
        raw_metadata = stream.find('.//w3af-version').text
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

    def parse_report(self, stream, scale):
        """Parse the report."""
        res = []
        for vuln in stream.findall('.//vulnerability'):
            info = Info(
                # Convert the severity of the issue thanks to an unified
                # ranking scale.
                ranking=scale[vuln.get('severity')],)
            res.append(info)
        return res
