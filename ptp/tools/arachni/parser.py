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
        r'(^0\.4\.[0-9]+$)|'
        r'(^1\.[0-9]+(\.[0-9]+)?$)')

    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    INFO = 'informational'

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    @classmethod
    def is_mine(cls, pathname, filename='*.xml', light=False, first=True):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool light: `True` to only parse the ranking of the findings from the report.
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
        if not self.check_version(self.metadata):
            raise NotSupportedVersionError('PTP does NOT support this version of Arachni.')
        return self.metadata

    def _parse_report_full(self, tree):
        """Parse Arachni XML reports to extract additional information.

        Arachni HTTP traffic is divided into following fields:
            * request
            * response status code
            * response headers
            * response body

        :return: List of dicts where each entry is the HTTP traffic generated for the issue.
        :rtype: :class:`list`

        """
        data = []
        for i in range(len(tree)):
            t_req = tree[i][1]
            t_res = tree[i][2]
            temp = t_req.find('.//body').text
            temp_body = '' if temp is None else temp
            # Somehow follow naming conventions from http://docs.python-requests.org/en/master/
            data.append({
                'request': t_req.find('.//raw').text + temp_body + '\n',
                'status_code': t_res.find('.//code').text,
                'headers': t_res.find('.//raw_headers').text.strip(),
                'body': t_res.find('.//body').text.strip()
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
        if not self.light:
            temp = []
            for record in self.stream.xpath('//variations//variation//referring_page'):
                temp.append(record.getchildren())
            self.vulns.append({'ranking': constants.UNKNOWN, 'transactions': self._parse_report_full(temp)})
        return self.vulns


class ArachniJSONParser(JSONParser):
    """Arachni XML specialized parser."""

    __tool__ = 'arachni'
    __format__ = 'xml'
    __version__ = r'(^1\.[0-9]+(\.[0-9]+)?$)'

    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    INFO = 'informational'

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    @classmethod
    def is_mine(cls, pathname, filename='*.json', light=False, first=True):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool light: `True` to only parse the ranking of the findings from the report.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename, first=first)
        except (TypeError, ValueError):
            return False
        if 'version' in stream:
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
        if not self.check_version(self.metadata):
            raise NotSupportedVersionError('PTP does NOT support this version of Arachni.')
        return self.metadata

    def _parse_report_full(self, issues):
        """Parse Arachni JSON reports to extract additional information.

        Arachni HTTP traffic is divided into following fields:
            * request
            * response status code
            * response headers
            * response body

        :return: List of dicts where each entry is the HTTP traffic generated for the issue.
        :rtype: :class:`list`

        """
        data = []
        for issue in issues:
            for variation in issue['variations']:
                temp_body = '' if variation['request']['body'] is None else variation['request']['body']
                # Somehow follow naming conventions from http://docs.python-requests.org/en/master/
                data.append({
                    'request': variation['request']['headers_string'] + temp_body + '\n',
                    'status_code': variation['response']['code'],
                    'header': variation['response']['headers_string'],
                    'body': variation['response']['body']
                })
        return data

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        self.vulns = [{'ranking': self.RANKING_SCALE[vuln['severity'].lower()]} for vuln in self.stream['issues']]
        if not self.light:
            self.vulns.append({'ranking': constants.UNKNOWN, 'transactions': self._parse_report_full(self.stream['issues'])})
        return self.vulns
