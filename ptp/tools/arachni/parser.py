"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the tool Arachni.

.. moduleauthor:: Tao Sauvage

"""

import re

from lxml.etree import XMLSyntaxError

from ptp.libptp import constants
from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.libptp.parser import XMLParser, JSONParser


class ArachniXMLParser(XMLParser):
    """Arachni XML specialized parser."""

    __tool__ = 'arachni'
    __format__ = 'xml'
    __version__ = (
        r'(^0\.4\.[6-7]{1}$)|'
        r'(^1\.0(\.[1-6]{1})?$)|'
        r'(^1\.1$)|'
        r'(^1\.2\.1$)')

    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    INFO = 'informational'

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    def __init__(self, pathname, filename='*.xml', http_parse=False, first=True):
        """Initialize ArachniXMLParser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        """
        XMLParser.__init__(self, pathname, filename, http_parse=http_parse, first=first)

    @classmethod
    def is_mine(cls, pathname, filename='*.xml', http_parse=False, first=True):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        :raises IOError: when the report file cannot be found.
        :raises OSError: when the report file cannot be found.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename, first=first)
        except (TypeError, XMLSyntaxError):
            return False
        except IOError as e:
            print(e.message)
            print("Moving to JSON parsing")
            return False
        version = stream.find('.//version')
        if version is None:
            return False
        if not re.findall(cls.__version__, version.text, re.IGNORECASE):
            return False
        return True

    def parse_metadata(self):
        """Parse the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support the version of this report.

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
            raise NotSupportedVersionError('PTP does NOT support this version of Arachni.')

    def get_data(self, tree):
        """XML file itself contains all requests and responses just needed to parse it correctly
        That is what this function does and return a list of dicts. HTTP traffic is divided into following fields
        * request
        * response status code
        * response headers
        * response body
        """
        data = []
        for i in range(len(tree)):
            t_req = tree[i][1]
            t_res = tree[i][2]
            # using max() function to get empty string if request body is None
            data.append({
                'request': t_req.find('.//raw').text + max(t_req.find('.//body').text, '') + '\n',
                'response_status_code': t_res.find('.//code').text,
                'response_headers': t_res.find('.//raw_headers').text.strip(),
                'response_body': t_res.find('.//body').text.strip()
            })
        return data

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        self.vulns = [
            {'ranking': self.RANKING_SCALE[vuln.find('.//severity').text.lower()]}
            for vuln in self.stream.find('.//issues')]
        if(self.__http_parse__):
            temp = []
            for record in self.stream.xpath('//variations//variation//referring_page'):
                temp.append(record.getchildren())
            self.vulns.append({'transactions': self.get_data(temp)})
        return self.vulns


class ArachniJSONParser(JSONParser):
    """Arachni XML specialized parser."""

    __tool__ = 'arachni'
    __format__ = 'xml'
    __version__ = (r'(^1\.2\.1$)')

    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    INFO = 'informational'

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    def __init__(self, pathname, filename='*.json', http_parse=False, first=True):
        """Initialize ArachniJSONParser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        """
        JSONParser.__init__(self, pathname, filename, http_parse=http_parse, first=first)

    @classmethod
    def is_mine(cls, pathname, filename='*.json', http_parse=False, first=True):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename, first=first)
        except (TypeError, XMLSyntaxError):
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
        """JSON file itself contains all requests and responses just needed to parse it correctly.

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
                    'request': variation['request']['headers_string'] + max(variation['request']['body'], '') + '\n',
                    'response_status_code': variation['response']['code'],
                    'response_header': variation['response']['headers_string'],
                    'response_body': variation['response']['body']
                })
        return data

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        self.vulns = [
            {'ranking': self.RANKING_SCALE[vuln['severity'].lower()]}
            for vuln in self.stream['issues']]

        if self.__http_parse__:
            self.vulns.append({'transactions': self.get_data(self.stream['issues'])})
        return self.vulns
