"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the
    tool Nmap.

.. moduleauthor:: Tao Sauvage

"""

from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.libptp.constants import UNKNOWN
from ptp.libptp.parser import XMLParser
from ptp.tools.nmap.signatures import SIGNATURES


class NmapXMLParser(XMLParser):

    __tool__ = 'nmap'
    __format__ = 'xml'
    __version__ = ['6.46']

    def __init__(self, pathname, filename='*.xml'):
        """Initialize NmapXMLParser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        XMLParser.__init__(self, pathname, filename)

    @classmethod
    def is_mine(cls, pathname, filename='*.xml'):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename)
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
                'PTP does NOT support this version of Nmap.')

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a vuln.
        :rtype: :class:`list`

        .. warning::

            Not implemented yet.

        """
        # TODO: Parse Nmap result
        ports = self.stream.findall('.//port')
        return []
