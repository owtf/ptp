"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the tool Arachni.

.. moduleauthor:: Tao Sauvage

"""

import re

from lxml.etree import XMLSyntaxError

from ptp.libptp import constants
from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.libptp.parser import JSONParser


class ArachniJSONParser(JSONParser):
    """Arachni XML specialized parser."""

    __tool__ = 'arachni'
    __format__ = 'xml'
    __version__ = (
        r'(^0\.4\.[6-7]{1}$)|'
        r'(^1\.0(\.[1-6]{1})?$)|'
        r'(^1\.1$)|'
        r'(^1\.2\.1)')

    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    INFO = 'informational'

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    def __init__(self, pathname, filename='*.json', first=True):
        """Initialize ArachniXMLParser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        """
        JSONParser.__init__(self, pathname, filename, first=first)

    @classmethod
    def is_mine(cls, pathname, filename='*.json', first=True):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename, first=first)
        except (IOError, TypeError, XMLSyntaxError):
            return False
        if stream.has_key('version'):
            version = stream['version']
        else:
            return False
        if not re.findall(cls.__version__, version, re.IGNORECASE):
            return False
        return True

    def parse_metadata(self):
        """Parse the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support the version of this report.

        :return: The metadata of the report.
        :rtype: dict

        """
        # Find the version of Arachni.
        version = self.stream['version']
        # Reconstruct the metadata
        # TODO: Retrieve the other metadata likes the date, etc.
        self.metadata = {'version': version}
        if self.check_version(self.metadata):
            return self.metadata
        else:
            raise NotSupportedVersionError('PTP does NOT support this version of Arachni.')

    def get_data(self, issues):
        """JSON file itself contains all requests and responses just needed to parse it correctly
        That is what this function does and return a list of dicts. HTTP traffic is divided into following fields
        * request
        * response status code
        * response headers
        * response body
        """
        data = []
        for issue in issues:
            for variation in issue['variations']:
                # using max() function to get empty string if request body is None
                data.append({
                    'request': variation['request']['headers_string']+max(variation['request']['body'], '')+'\n',
                    'response_status_code': variation['response']['code'],
                    'response_header': variation['response']['headers_string'],
                    'response_body': variation['response']['body']
                })
        return data

    def parse_report(self, full_parse):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        self.vulns = [
            {'ranking': self.RANKING_SCALE[vuln['severity'].lower()]}
            for vuln in self.stream['issues']]

        if full_parse:
            self.data = self.get_data(self.stream['issues'])
            return self.vulns, self.data
        return self.vulns
