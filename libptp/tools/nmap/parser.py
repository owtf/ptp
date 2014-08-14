"""

:synopsis: Specialized Parser classes for the tool Nmap.

.. moduleauthor:: Tao Sauvage

"""

from libptp.exceptions import NotSupportedVersionError
from libptp.constants import UNKNOWN
from libptp.parser import XMLParser
from libptp.tools.nmap.signatures import SIGNATURES


class NmapXMLParser(XMLParser):

    #: :class:`str` -- Name of the tool.
    __tool__ = 'nmap'
    #: :class:`str` -- Format of Nmap reports it supports.
    __format__ = 'xml'
    #: :class:`list` -- Nmap versions it supports.
    __version__ = ['6.46']

    def __init__(self, fullpath):
        XMLParser.__init__(self, fullpath)

    @classmethod
    def is_mine(cls, fullpath):
        """Check if it is a supported Nmap report.

        :param str pathname: Path to the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(fullpath)
        except ValueError:
            return False
        if stream.get('scanner') != cls.__tool__:
            return False
        if not stream.get('version') in cls.__version__:
            return False
        return True

    def parse_metadata(self):
        """Parse the metadatas of the report.

        :return: The metadatas of the report.
        :rtype: dict

        :raises: :class:`NotSupportedVersionError` -- if it does not support
            the version of this report.

        """
        # Find the metadata of Nmap.
        metadata = {key: value for key, value in self.stream.items()}
        if self.check_version(metadata):
            self.metadata = metadata
        else:
            raise NotSupportedVersionError(
                'PTP does NOT support this version of ' + self.__tool__ + '.')

    # TODO: Parse Nmap result
    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a vuln.
        :rtype: :class:`list`

        """
        ports = self.stream.findall('.//port')
        return []
