"""

:synopsis: Specialized Report class for the tool DirBuster.

.. moduleauthor:: Tao Sauvage

"""

from libptp.report import AbstractReport
from libptp.tools.dirbuster.parser import DirbusterParser


class DirbusterReport(AbstractReport):
    """Retrieve the information of a DirBuster report."""

    #: :class:`str` -- Name of the tool.
    __tool__ = 'dirbuster'
    #: :class:`list` -- Available parsers for DirBuster.
    __parsers__ = [DirbusterParser]

    def __init__(self):
        """Initialize DirbusterReport."""
        AbstractReport.__init__(self)

    @classmethod
    def is_mine(cls, pathname, filename='DirBuster-Report*'):
        """Check if it is a DirBuster report and if it can handle it.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        fullpath = cls._recursive_find(pathname, filename)
        if not fullpath:
            return False
        fullpath = fullpath[0]  # Only keep the first file.
        # TODO: Properly check if it is a DirBuster report.
        return AbstractReport._is_parser(cls.__parsers__, fullpath)

    def parse(self, pathname=None, filename='DirBuster-Report*'):
        """Parse a Dirbuster report.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: List of dicts where each one represents a vuln.
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
        # TODO: Return something like an unified version of the report.
        return self.vulns
