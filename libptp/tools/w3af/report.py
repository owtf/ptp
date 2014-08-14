"""

:synopsis: Specialized Report class for W3AF.

.. moduleauthor:: Tao Sauvage

"""

from libptp.report import AbstractReport
from libptp.tools.w3af.parser import W3AFXMLParser


class W3AFReport(AbstractReport):
    """Retrieve the information of a W3AF report."""

    #: :class:`str` -- Name of the tool.
    __tool__ = 'w3af'
    #: :class:`list` -- Available parsers for W3AF.
    __parsers__ = [W3AFXMLParser]

    def __init__(self, *args, **kwargs):
        """Initialize W3AFReport."""
        AbstractReport.__init__(self, *args, **kwargs)

    @classmethod
    def is_mine(cls, pathname, filename='*.xml'):
        """Check if it is a W3AF report and if it can handle it.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        return AbstractReport.is_mine(
            cls.__parsers__,
            pathname=pathname,
            filename=filename)

    def parse(self, pathname, filename='*.xml'):
        """Parse a W3AF report.

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
