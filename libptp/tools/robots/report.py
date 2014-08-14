"""

:synopsis: Specialized Report class for Reports.txt.

.. moduleauthor:: Tao Sauvage

"""

from libptp.report import AbstractReport
from libptp.tools.robots.parser import RobotsParser


class RobotsReport(AbstractReport):
    """Retrieve the information of a Robots.txt report."""

    __tool__ = 'robots'
    __parsers__ = [RobotsParser]

    def __init__(self):
        """Initialize RobotsReport."""
        AbstractReport.__init__(self)

    @classmethod
    def is_mine(cls, pathname, filename='*.txt'):
        """Check if it is a robot.txt report and if it can handle it.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        return AbstractReport.is_mine(
            cls.__parsers__,
            pathname=pathname,
            filename=filename)

    def parse(self, pathname, filename='*.txt'):
        """Parse a Robots.txt report.

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
