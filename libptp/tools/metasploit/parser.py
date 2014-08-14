"""

:synopsis: Specialized Parser classes for Metasploit.

.. moduleauthor:: Tao Sauvage

"""

from libptp.parser import FileParser
from libptp.tools.metasploit.signatures import SIGNATURES


class MetasploitParser(FileParser):
    """Metasploit specialized parser."""

    __tool__ = 'metasploit'
    __plugin__ = ''

    def __init__(self, fullpath, plugin=''):
        """Initialize MetasploitParser.

        :param str fullpath: Full path to the report file.
        :param str plugin: Name of the plugin that generated the report.

        """
        FileParser.__init__(self, fullpath)
        self.__plugin__ = plugin

    @classmethod
    def is_mine(cls, fullpath, plugin=''):
        """Check if it is a supported Metasploit report.

        :param str fullpath: Full path to the report file.
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
