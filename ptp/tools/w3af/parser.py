"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the tool W3AF.

.. moduleauthor:: Tao Sauvage

"""

import re

from lxml.etree import XMLSyntaxError

from ptp.libptp import constants
from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.libptp.parser import XMLParser, FileParser


class W3AFXMLParser(XMLParser):
    """W3AF XML specialized parser."""

    __tool__ = 'w3af'
    __format__ = 'xml'
    __httpfile_format__ = "*.http.txt"
    __version__ = (
        r'(1\.6(\.0\.[1-5]{1})?)|'
        r'(1\.6\.([45,46,49,50,51]{1})?)')

    _re_version = re.compile(r'Version: (\S*)\s')
    _re_transaction = re.compile(r"(?<=={30}Request )[0-9]+ .*?={9}\n(.*?)(?=\n={70})", re.S)
    _re_request = re.compile(r"(^.*?)\n==.*?(?=={20}Response )", re.S)
    _re_response = re.compile(r"(?<=={40}Response )[0-9]+ .*?={9}\n(\w.*)", re.S)
    _re_reponse_header = re.compile(r".*?content-type: .*?\n", re.S)
    _re_response_body = re.compile(r"(?<=content-type: )(.*?\n)(.*)", re.S)
    _re_response_status_code = re.compile(r"(?<=HTTP/\w.\w )(.*)")

    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
    INFO = 'Information'

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        INFO: constants.INFO}

    def __init__(self, pathname, filename='*.xml', http_parse=False, first=True):
        """Initialize W3AFXMLParser.

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
        cls.pathname = pathname # pathname is used later so making it accessible
        try:
            stream = cls.handle_file(pathname, filename, first=first)
        except (TypeError, XMLSyntaxError):
            return False
        version = stream.find('.//w3af-version')
        if version is None:
            return False
        version = cls._re_version.findall(version.text)
        if not version:
            return False
        if len(version) >= 1:  # In case we found several version numbers.
            version = version[0]
        if not re.findall(cls.__version__, version, re.IGNORECASE):
            return False
        return True

    def parse_metadata(self):
        """Parse the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support the version of this report.

        :return: The metadata of the report.
        :rtype: dict

        """
        raw_metadata = self.stream.find('.//w3af-version').text
        # Find the version of w3af.
        version = self._re_version.findall(raw_metadata)
        if len(version) >= 1:  # In case we found several version numbers.
            version = version[0]
        # Reconstruct the metadata
        # TODO: Retrieve the other metadata likes the date, etc.
        metadata = {'version': version}
        if self.check_version(metadata):
            self.metadata = metadata
        else:
            raise NotSupportedVersionError('PTP does NOT support this version of W3AF.')
        return self.metadata

    def parse_http(self, raw_transdata):
        """Parse the captured http transactions of the report.

        :return: List of dicts where each one has a request and response.
        :rtype: :class:`list`

        """
        data = []
        transactions = self._re_transaction.findall(raw_transdata)
        for count, transaction in enumerate(transactions):
            response = self._re_response.findall(transaction)[0] + '\n'
            response_header = self._re_reponse_header.search(response).group()
            data.append({
                'request': self._re_request.findall(transaction)[0].strip() + '\n\n',
                'response_status_code': self._re_response_status_code.search(response_header).group(),
                'response_headers': response_header,
                'response_body': self._re_response_body.search(response).group(2)
            })
        return data

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one represents a discovery.
        :rtype: :class:`list`

        """
        self.vulns = [
            {'ranking': self.RANKING_SCALE[vuln.get('severity')]}
            for vuln in self.stream.findall('.//vulnerability')]
        if self.__http_parse__:
            self.vulns.append({'transactions': self.parse_http(FileParser.handle_file(self.pathname, '*.http.txt'))})
        return self.vulns
