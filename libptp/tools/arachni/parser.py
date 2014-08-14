"""

:synopsis: Specialized Parser classes for the tool Arachni.

.. moduleauthor:: Tao Sauvage

"""

from lxml.etree import LxmlError

from libptp.exceptions import NotSupportedVersionError
from libptp.parser import XMLParser


class ArachniXMLParser(XMLParser):
    """Arachni XML specialized parser."""

    #: :class:`str` -- Name of the tool.
    __tool__ = 'arachni'
    #: :class:`str` -- Format of Arachni reports it supports.
    __format__ = 'xml'
    #: :class:`list` -- Versions of Arachni that are supported.
    __version__ = ['0.4.6', '0.4.7']

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

    def parse_report(self, scale):
        """Parse the results of the report.

        :param dict scale: Unified scale between Arachni and PTP.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        self.vulns = [
            {'ranking': scale[vuln.find('.//severity').text]}
            for vuln in self.stream.find('.//issues')]
        return self.vulns
