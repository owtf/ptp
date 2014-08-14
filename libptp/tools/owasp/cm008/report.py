"""

:synopsis: Specialized Report class for OWASP-CM-008 test.

.. moduleauthor:: Tao Sauvage

"""

from libptp.report import AbstractReport
from libptp.tools.owasp.cm008.parser import OWASPCM008Parser


class OWASPCM008Report(AbstractReport):
    """Retrieve the information of the OWASP-CM-008 test."""

    #: :class:`str` -- Name of the tool.
    __tool__ = 'owasp-cm-008'
    #: :class:`list` -- Available parsers for OWASP-CM-008.
    __parsers__ = [OWASPCM008Parser]

    def __init__(self):
        """Initialize OWASPCM008Report."""
        AbstractReport.__init__(self)

    @classmethod
    def is_mine(cls, pathname, filename='*.txt'):
        """Check if it is an OWASP-CM-008 report and if it can handle it.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        fullpath = cls._recursive_find(pathname, filename)
        if not fullpath:
            return False
        fullpath = fullpath[0]  # Only keep the first file.
        return AbstractReport._is_parser(cls.__parsers__, fullpath)

    def parse(self, pathname, filename='*.txt'):
        """Parse an OWASP-CM-008 report.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: List of dicts where each one represents a discovery from the
            report.
        :rtype: :class:`list`

        """
        # Reconstruct the path to the report if any.
        self.fullpath = self._recursive_find(pathname, filename)
        if not self.fullpath:
            return []
        self.fullpath = self.fullpath[0]
        # Find the corresponding parser.
        self._init_parser(self.fullpath)
        # Parse specific stuff.
        self.metadata = self.parser.parse_metadata()
        self.vulns = self.parser.parse_report()
        return self.vulns
