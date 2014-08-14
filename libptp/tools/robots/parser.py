"""

:synopsis: Specialized Parser class for Robots.txt.

.. moduleauthor:: Tao Sauvage

"""

from libptp.constants import UNKNOWN
from libptp.parser import LineParser
from libptp.tools.robots.signatures import SIGNATURES


class RobotsParser(LineParser):
    """Robots specialized parser."""

    __tool__ = 'robots'
    __format__ = 'txt'

    def __init__(self, pathname, filename='*.txt'):
        """Initialize RobotsParser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        LineParser.__init__(self, pathname, filename)

    @classmethod
    def is_mine(cls, pathname, filename='*.txt'):
        """Check if it is a supported robots.txt report.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename)
        except (OSError, IOError, ValueError):
            return False
        if stream and stream[0].startswith('User-agent'):
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
        """Parser the results of a Robots.txt report.

        :return: List of dicts where each one represents a vuln.
        :rtype: :class:`list`

        """
        disallowed_entries = [
            line.lstrip('Disallow: ')
            for line in self.stream
            if line.startswith('Disallow')]
        if not disallowed_entries:
            return []
        self.vulns = [
            {'ranking': SIGNATURES.get(entry, UNKNOWN)}
            for entry in disallowed_entries]
        return self.vulns
