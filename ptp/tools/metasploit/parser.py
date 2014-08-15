"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the
    tool Metasploit.

.. moduleauthor:: Tao Sauvage

"""

from ptp.libptp.parser import FileParser
from ptp.tools.metasploit.signatures import SIGNATURES


class MetasploitParser(FileParser):
    """Metasploit specialized parser."""

    __tool__ = 'metasploit'
    __plugin__ = ''

    def __init__(self, pathname, filename='*.txt', plugin=''):
        """Initialize MetasploitParser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param str plugin: Name of the plugin that generated the report.

        """
        self.__plugin__ = plugin
        FileParser.__init__(self, pathname, filename)

    @classmethod
    def is_mine(cls, pathname, filename='*.txt', plugin=''):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param str plugin: Name of the plugin that generated the report.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        # TODO: Properly check the supported versions.
        if plugin:
            return True
        return False

    def parse_metadata(self):
        """Parse the metadata of the report.

        :return: The metadata of the report.
        :rtype: dict

        """
        # TODO: Properly retrieve the metadata.
        return {}

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        try:
            signatures = SIGNATURES.get(self.__plugin__, {}).iteritems()
        except AttributeError:  # Python3
            signatures = SIGNATURES.get(self.__plugin__, {}).items()
        self.vulns = [{
            'name': self.__plugin__,
            'ranking': ranking}
            for signature, ranking in signatures
            if signature in self.stream]
        return self.vulns
