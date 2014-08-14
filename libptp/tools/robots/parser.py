"""

:synopsis: Specialized Parser class for Robots.txt.

.. moduleauthor:: Tao Sauvage

"""

import re

from libptp.constants import UNKNOWN
from libptp.parser import LineParser
from libptp.tools.robots.signatures import SIGNATURES


class RobotsParser(LineParser):
    """Robots specialized parser."""
    #: :class:`str` -- Name of the tool.
    __tool__ = 'robots'
    #: :class:`str` -- Format of Robots reports it supports.
    __format__ = 'txt'

    def __init__(self, fullpath):
        """Initialize RobotsParser.

        :param str fullpath: full path to the report file.

        """
        LineParser.__init__(self, fullpath)

    # TODO: Properly check the supported versions.
    @classmethod
    def is_mine(cls, fullpath, filename='*.txt'):
        try:
            stream = cls.handle_file(fullpath)
        except (OSError, IOError):
            return False
        if stream and stream[0].startswith('User-agent'):
            return True
        return False

    def parse_metadata(self):
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
        return [
            {'ranking': SIGNATURES.get(entry, UNKNOWN)}
            for entry in disallowed_entries]
