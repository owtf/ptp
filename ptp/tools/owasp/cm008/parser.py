"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the
    tool OWASP-CM-008.

.. moduleauthor:: Tao Sauvage

"""

import re

from ptp.libptp.constants import UNKNOWN
from ptp.libptp.parser import LineParser
from ptp.tools.owasp.cm008.signatures import SIGNATURES


class OWASPCM008Parser(LineParser):
    """OWASPCM008 specialized parser."""

    __tool__ = 'owasp-cm-008'

    def __init__(self, pathname, filename='*.txt'):
        """Initialize OWASPCM008Parser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        LineParser.__init__(self, pathname, filename)

    @classmethod
    def is_mine(cls, pathname, filename='*.txt'):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename)
        except (OSError, IOError, ValueError):
            return False
        if stream and stream[0].startswith('HTTP'):
            return True
        return False

    def parse_metadata(self):
        """Parse the metadata of the report.

        :return: The metadata of the report.
        :rtype: dict

        """
        self.metadata = {
            'date': line.lstrip('Date: ')
            for line in self.stream
            if line.startswith('Date')}
        return self.metadata

    def parse_report(self):
        """Parser the results of OWASP-CM-008 results.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        allowed_methods = [
            line.lstrip('Allow: ').split(', ')
            for line in self.stream
            if line.startswith('Allow')][0]
        if not allowed_methods:
            return []
        self.vulns = [
            {'ranking': SIGNATURES.get(method, UNKNOWN)}
            for method in allowed_methods]
        return self.vulns
