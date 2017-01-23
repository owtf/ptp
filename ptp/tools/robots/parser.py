"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the robots.txt files.

.. moduleauthor:: Tao Sauvage

"""

from ptp.libptp.constants import UNKNOWN
from ptp.libptp.parser import LineParser
from ptp.tools.robots.signatures import SIGNATURES


class RobotsParser(LineParser):
    """Robots specialized parser."""

    __tool__ = 'robots'
    __format__ = 'txt'

    def __init__(self, pathname, filename='*robots.txt', light=False, first=True):
        LineParser.__init__(self, pathname, filename, light=light, first=first)

    @classmethod
    def is_mine(cls, pathname, filename='*robots.txt', light=False, first=True):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool light: `True` to only parse the ranking of the findings from the report.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        :raises IOError: when the report file cannot be found.
        :raises OSError: when the report file cannot be found.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        stream = cls.handle_file(pathname, filename, first=first)
        if stream and stream[0].startswith(('User-agent:', 'Disallow:', 'Allow:')):  # FIXME: Weak check here...
            return True
        return False

    def parse_metadata(self):
        """Parse the metadata of the report.

        :return: The metadata of the report.
        :rtype: dict

        """
        return {}  # No metadata to retrieve in robots.txt

    def parse_report(self):
        """Parser the results of a Robots.txt report.

        :return: List of dicts where each one represents a vuln.
        :rtype: :class:`list`

        """
        disallowed_entries = [line.lstrip('Disallow: ') for line in self.stream if line.startswith('Disallow')]
        if not disallowed_entries:
            return []
        self.vulns = [
            {'ranking': SIGNATURES.get(entry, UNKNOWN)}
            for entry in disallowed_entries]
        return self.vulns
