"""

:synopsis: Specialized Report class for the tool Arachni.

.. moduleauthor:: Tao Sauvage

"""

from libptp import constants
from libptp.report import AbstractReport
from libptp.tools.arachni.parser import ArachniXMLParser


class ArachniReport(AbstractReport):
    """Retrieve the information of an Arachni report."""

    #: :class:`str` -- Name of the tool.
    __tool__ = 'arachni'
    #: :class:`list` -- Available parsers for Arachni.
    __parsers__ = [ArachniXMLParser]

    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    INFO = 'Informational'

    #: :class:`dict` -- Convert the Arachni's ranking scale to an unified one.
    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    def __init__(self):
        """Initialize ArachniReport."""
        AbstractReport.__init__(self)

    @classmethod
    def is_mine(cls, pathname, filename='*.xml'):
        """Check if it is an Arachni report and if it can handle it.

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
        """Parse an Arachni report.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the XML report file.

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
        self.vulns = self.parser.parse_report(self.RANKING_SCALE)
        print('#Debug Arachni parse', self.vulns)
        return self.vulns
