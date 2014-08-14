"""

:synopsis: Specialized Parser classes for the tool Arachni.

.. moduleauthor:: Tao Sauvage

"""

from lxml.etree import LxmlError

from libptp import constants
from libptp.exceptions import NotSupportedVersionError
from libptp.parser import XMLParser


class ArachniXMLParser(XMLParser):
    """Arachni XML specialized parser."""

    __tool__ = 'arachni'
    __format__ = 'xml'
    __version__ = ['0.4.6', '0.4.7']

    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    INFO = 'Informational'

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    def __init__(self, fullpath):
        """Initialize ArachniXMLParser.

        :param str fullpath: full path to the report file.

        """
        XMLParser.__init__(self, fullpath)

    @classmethod
    def is_mine(cls, fullpath):
        """Check if it is a supported Arachni report.

        :param str fullpath: full path to the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(fullpath)
        except (ValueError, LxmlError):
            return False
        if not cls.__tool__ in stream.tag:
            return False
        return True

    def parse_metadata(self):
        """Parse the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support
            the version of this report.

        :return: The metadata of the report.
        :rtype: dict

        """
        # Find the version of Arachni.
        version = self.stream.find('.//version')
        # Reconstruct the metadata
        # TODO: Retrieve the other metadata likes the date, etc.
        self.metadata = {version.tag: version.text}
        if self.check_version(self.metadata):
            return self.metadata
        else:
            raise NotSupportedVersionError(
                'PTP does NOT support this version of Arachni.')

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        self.vulns = [
            {'ranking': self.RANKING_SCALE[vuln.find('.//severity').text]}
            for vuln in self.stream.find('.//issues')]
        return self.vulns
