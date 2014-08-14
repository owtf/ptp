"""

:synopsis: Specialized Parser classes for OWASP-CM-008.

.. moduleauthor:: Tao Sauvage

"""

import re

from libptp.constants import UNKNOWN
from libptp.parser import LineParser
from libptp.tools.owasp.cm008.signatures import SIGNATURES


class OWASPCM008Parser(LineParser):
    """OWASPCM008 specialized parser."""

    __tool__ = 'owasp-cm-008'

    def __init__(self, fullpath):
        """Initialize ArachniXMLParser.

        :param str fullpath: full path to the report file.

        """
        LineParser.__init__(self, fullpath)

    @classmethod
    def is_mine(cls, fullpath):
        """Check if it is a supported OWASP-CM-008 report.

        :param str fullpath: full path to the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(fullpath)
        except (OSError, IOError):
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
