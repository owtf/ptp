"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the tool OWASP-CM-008.

.. moduleauthor:: Tao Sauvage

"""

from ptp.libptp.constants import UNKNOWN
from ptp.libptp.parser import LineParser
from ptp.tools.owasp.cm008.signatures import SIGNATURES


class OWASPCM008Parser(LineParser):
    """OWASPCM008 specialized parser."""

    __tool__ = 'owasp-cm-008'

    @classmethod
    def is_mine(cls, pathname, filename='*', light=True, first=False):
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
        if stream and stream[0].startswith('HTTP'):  # FIXME: Weak check here...
            return True
        return False

    def parse_metadata(self):
        """Parse the metadata of the report.

        :return: The metadata of the report.
        :rtype: dict

        """
        self.metadata = {'date': line.lstrip('Date: ') for line in self.stream if line.startswith('Date')}
        return self.metadata

    def parse_report(self):
        """Parser the results of OWASP-CM-008 results.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        allowed_methods = [
            line.lstrip('Allow: ').split(', ')
            for line in self.stream
            if line.startswith('Allow')]
        if not allowed_methods:
            return []
        self.vulns = [
            {'ranking': SIGNATURES.get(method, UNKNOWN)}
            for methods in allowed_methods
            for method in methods]
        return self.vulns
