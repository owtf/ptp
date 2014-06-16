from libptp.exceptions import NotSupportedVersionError
from libptp.info import Info
from libptp.parser import AbstractParser


class ArachniXMLParser(AbstractParser):

    __tool__ = 'arachni'
    __format__ = 'xml'
    __version__ = ['0.4.6']

    def __init__(self, *args, **kwargs):
        AbstractParser.__init__(self, *args, **kwargs)

    @classmethod
    def is_mine(cls, stream):
        """Check if it is a supported report."""
        if not cls.__tool__ in stream.tag:
            return False
        return True

    def parse_metadata(self, stream):
        """Parse the metadatas of the report."""
        # Find the version of Arachni.
        version = stream.find('.//version')
        # Reconstruct the metadata
        # TODO: Retrieve the other metadata likes the date, etc.
        metadata = {version.tag: version.text,}
        if self.check_version(metadata):
            return metadata
        else:
            raise NotSupportedVersionError(
                'PTP does NOT support this version of Arachni.')

    def parse_report(self, stream, scale):
        """Parse the report."""
        res = []
        vulns = stream.find('.//issues')
        for vuln in vulns.findall('.//issue'):
            info = Info(
                # Convert the severity of the issue thanks to an unified
                # ranking scale.
                ranking=scale[vuln.find('.//severity').text],)
            res.append(info)
        return res
