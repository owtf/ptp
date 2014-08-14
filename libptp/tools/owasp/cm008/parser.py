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
    #: :class:`str` -- Name of the tool.
    __tool__ = 'owasp-cm-008'

    def __init__(self, fullpath):
        LineParser.__init__(self, fullpath)

    # TODO: Properly check the supported versions.
    @classmethod
    def is_mine(cls, fullpath):
        stream = cls.handle_file(pathname)
        if stream and stream[0].startswith('HTTP'):
            return True
        return False

    # TODO: Properly retrieve the metadatas.
    def parse_metadata(self):
        return {
            'date': line.lstrip('Date: ')
            for line in self.stream
            if line.startswith('Date')}

    def parse_report(self):
        """Parser the results of OWASP-CM-008 results.

        :return: List of dicts where each one represents a vuln.
        :rtype: :class:`list`

        """
        allowed_methods = [
            line.lstrip('Allow: ').split(', ')
            for line in self.stream
            if line.startswith('Allow')][0]
        if not allowed_methods:
            return []
        return [
            {'ranking': SIGNATURES.get(method, UNKNOWN)}
            for method in allowed_methods]
