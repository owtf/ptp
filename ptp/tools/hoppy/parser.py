"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the tool Hoppy.

.. moduleauthor:: DoomTaper

"""

import re

from ptp.libptp import constants
from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.libptp.parser import FileParser


class HoppyParser(FileParser):
    """Hoppy specialized parser."""

    __tool__ = 'hoppy'
    __version__ = r'1\.[0-9]+(\.[0-9]+)?'

    _re_version = re.compile(r"\D{3} \S+ (\d\.\d+\.\d+) \S")
    _re_transaction = re.compile(r"(?<=We Sent:)\n.*?(\S+ /.*?)\n(?=\n\t\D{3} Parsed Response:)", re.S)
    _re_request = re.compile(r"(\S+ /.*?)\n(?=Server)", re.S)
    _re_response = re.compile(r"(?<=Responded:\n\n)(.*)", re.S)
    _re_response_status_code = re.compile(r"(?<=HTTP/\w.\w )(.*)")
    _re_response_parse = re.compile(r"(?P<headers>HTTP.*?)\n(?=\r\n)(?P<body>.*)", re.S)

    def __init__(self, pathname, filename='*.spider', **kwargs):
        """Initialize HoppyParser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        FileParser.__init__(self, pathname, filename, **kwargs)

    @classmethod
    def is_mine(cls, pathname, filename='*.summary', light=False, first=True):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool light: `True` to only parse the ranking of the findings from the report.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        cls.pathname = pathname
        try:
            stream = cls.handle_file(pathname, filename, first=first)
        except (TypeError):
            return False
        version = cls._re_version.findall(stream)
        if not version:
            return False
        if len(version) >= 1:  # In case we found several version numbers.
            version = version[0]
        if not re.findall(cls.__version__, version, re.IGNORECASE):
            return False
        cls.version = version
        return True

    def parse_metadata(self):
        """Parse the metadata of the report.

        :raises: :class:`NotSupportedVersionError` -- if it does not support the version of this report.

        :return: The metadata of the report.
        :rtype: dict

        """
        # TODO: Retrieve the other metadata likes the date, etc.
        metadata = {'version': self.version}
        if self.check_version(metadata):
            self.metadata = metadata
        else:
            raise NotSupportedVersionError('PTP does NOT support this version of Hoppy.')
        return self.metadata

    def parse_report(self):
        """Parse the results of the report.

        :return: List of dicts where each one has a request and response.
        :rtype: :class:`list`

        """
        self.data = []
        data = []
        transactions = self._re_transaction.findall(self.stream)
        if not transactions:
            return None
        for count, transaction in enumerate(transactions):
            response = self._re_response.search(transaction).group().strip() + '\n\n'
            status_code = self._re_response_status_code.findall(response)
            parsed_response = self._re_response_parse.findall(response)
            # Somehow follow naming conventions from http://docs.python-requests.org/en/master/
            data.append({
                'request': self._re_request.findall(transaction)[0].strip() + '\n\n',
                'status_code': status_code[0].strip() + '\n',
                'headers': parsed_response[0][0].strip() + '\n\n',
                'body': parsed_response[0][1].strip() + '\n\n'
            })
        self.data.append({'ranking': constants.UNKOWN, 'transactions': data})
        return self.data
