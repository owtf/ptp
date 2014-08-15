"""

:synopsis: Specialized :class:`ptp.libptp.parser.AbstractParser` classes for the
    tool DirBuster.

.. moduleauthor:: Tao Sauvage

"""

import re

from ptp.libptp.parser import LineParser
from ptp.tools.dirbuster.signatures import DIRECTORIES, FILES


class DirbusterParser(LineParser):
    """DirBuster specialized parser."""

    __tool__ = 'dirbuster'
    __format__ = 'dirbuster'
    __version__ = ['1.0-RC1']

    #: :class:`str` -- Regex matching DirBuster section separator.
    _re_sep = r"^-*$"
    #: :class:`str` -- Regex matching DirBuster version.
    _re_version = r"^DirBuster (?P<version>[0-9]+\.[0-9]+(-RC[0-9])?) - Report$"
    #: :class:`str` -- Regex matching DirBuster directories status code.
    _re_dir_status = r"^Dirs found with a (?P<status>[0-9]{3}) response:$"
    #: :class:`str` -- Regex matching DirBuster files status code.
    _re_file_status = r"^Files found with a (?P<status>[0-9]{3}) responce:$"

    def __init__(self, pathname, filename='DirBuster-Report*'):
        """Initialize DirbusterParser.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        LineParser.__init__(self, pathname, filename)

    @classmethod
    def is_mine(cls, pathname, filename='DirBuster-Report*'):
        """Check if it can handle the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :return: `True` if it supports the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        try:
            stream = cls.handle_file(pathname, filename)
        except (OSError, IOError, ValueError):
            return False
        if stream and re.match(cls._re_version, stream[0]):
            return True
        return False

    def parse_metadata(self):
        """Parse the metadata of the report.

        :return: The metadata of the report.
        :rtype: dict

        """
        # TODO: Properly retrieve the metadata.
        return {}

    def parse_report(self):
        """Parser the results of a DirBuster report.

        :return: List of dicts where each one represents a vuln.
        :rtype: :class:`list`

        """
        # Retrieve the results from the report.
        discoveries = {'directories': [], 'files': [], 'errors': []}
        type_disco = 'errors'
        status_code = -1
        for line in self.stream:
            match_dir_status = re.match(self._re_dir_status, line)
            match_file_status = re.match(self._re_file_status, line)
            if match_dir_status:
                type_disco = 'directories'
                status_code = match_dir_status.group('status')
            elif match_file_status:
                type_disco = 'files'
                status_code = match_file_status.group('status')
            elif line.startswith('/'):  # This line contains a discovery
                status = int(status_code)
                # If this is the section of the successful ones (2xx).
                if status >= 200 and status < 300:
                    discoveries[type_disco].append(line)
        # Match found discoveries against signatures database.
        vulns = []
        matching = ((DIRECTORIES, 'directories'), (FILES, 'files'))
        for signatures, type_disco in matching:
            try:
                signatures = signatures.iteritems()
            except AttributeError:  # Python3
                signatures = signatures.items()
            for signature, ranking in signatures:
                matched = [
                    True
                    for disco in discoveries[type_disco]
                    if re.match(signature, disco)]
                if True in matched:
                    vulns.extend([{'ranking': ranking}])
        self.vulns = vulns
        return vulns
