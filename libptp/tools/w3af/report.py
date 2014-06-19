from libptp import constants
from libptp.report import AbstractReport
from libptp.tools.w3af.parser import W3AFXMLParser


class W3AFReport(AbstractReport):
    """Retrieve the information of a w3af report."""

    __tool__ = 'w3af'
    __parsers__ = {W3AFXMLParser: '1.6.0.2'}

    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    INFO = 'Information'

    # Convert the W3AF's ranking scale to an unified one.
    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    def __init__(self, *args, **kwargs):
        AbstractReport.__init__(self, *args, **kwargs)

    @classmethod
    def is_mine(cls, pathname, filename='*.xml'):
        """Check if it is a W3af report and if I can handle it.

        Return True if it is mine, False otherwise.

        """
        fullpath = cls._recursive_find(pathname, filename)
        if not fullpath:
            return False
        fullpath = fullpath[0]  # Only keep the first file.
        return AbstractReport._is_parser(fullpath, cls.__parsers__)

    def parse(self, pathname=None, filename='*.xml'):
        """Parse a w3af resport."""
        # Reconstruct the path to the report if any.
        self.fullpath = self._recursive_find(pathname, filename)[0]
        # Find the corresponding parser.
        self._init_parser(self.fullpath)
        # Parse specific stuff.
        self.metadata = self.parser.parse_metadata()
        self.vulns = self.parser.parse_report(self.RANKING_SCALE)
        # TODO: Return something like an unified version of the report.
        return self.vulns
