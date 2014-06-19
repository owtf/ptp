"""

.. module:: report
    :synopsis: The Report class will be the summary of a complete report
               provided by a pentesting tool.

.. moduleauthor:: Tao Sauvage

"""


import os
import fnmatch

from libptp.exceptions import NotSupportedVersionError
from libptp.constants import RANKING_SCALE


class AbstractReport(object):

    """Abstract representation of a report provided by a pentesting tool.

    .. note::

        This class will be extended for each pentesting tool. That way, each
        tool will add its own report/parsing specificities.

    """

    #: Supported versions of the tool.
    __version__ = None
    #: Available parsers for the tool.
    __parsers__ = None

    def __init__(self, vulns=None):
        """Self-explanatory."""
        #: The current parser the report is using.
        self.parser = None
        #: List of dictionaries of the results found in the report.
        self.vulns = [] or vulns

    def __str__(self):
        return ', '.join([info.__str__() for info in self.vulns])

    @classmethod
    def is_mine(cls, pathname, filename=None):
        """Check if it is a report from the tool this class supports.

        :param pathname: The path to the report.
        :type pathname: str.
        :param filename: The name of the report file.
        :type filename: str.

        :returns: bool -- `True` if this class supports this tool, `False`
                  otherwise

        """
        return False

    @classmethod
    def _is_parser(cls, pathname, parsers):
        """Check if a parser exists for that report.

        :param pathname: Path to the report file.
        :type pathname: str.
        :param parsers: The available parsers of this class.
        :type parsers: AbstractParser.

        :returns: bool -- `True` if this class has a parser for this tool,
                  `False` otherwise

        """
        if parsers is not None:
            for parser in iter(parsers):
                if parser.is_mine(pathname):
                    return True
        return False

    @classmethod
    def check_version(cls, metadata, key='version'):
        """Checks the version from the metadata against the supported ones.

        :param metadata: The metadata in which to find the version.
        :type metadata: dict.
        :param key: The :attr:`metadata` key containing the version value.
        :type key: str.

        :returns: bool -- `True` if it support that version, `False` otherwise.

        """
        if metadata[key] in cls.__parsers__.itervalues():
            return True
        return False

    @staticmethod
    def _recursive_find(pathname='./', file_regex='*', early_break=True):
        """Retrieve the full path to the report.

        The search occurs in the directory `pathname`.
        :param pathname: The root directory where to start the search.
        :type pathname: str.
        :param file_regex: The regex that will be matched against all files
                           from within `pathname`.
        :type file_regex: re.
        :param early_break: Stop the search as soon as a file has been matched.
        :type early_break: bool.

        :returns: list -- A list of paths to matched files starting from
                  `pathname`.

        """
        founds = []
        for base, _, files in os.walk(pathname):
            matched_files = fnmatch.filter(files, file_regex)
            founds.extend(
                os.path.join(base, matched_file)
                for matched_file in matched_files)
            if founds and early_break:
                break
        return founds

    def _init_parser(self, pathname):
        """Instantiate the correct parser for the report.

        :param pathname: path to the report.
        :type pathname: str.
        :raises: NotSupportedVersionError

        """
        for parser in iter(self.__parsers__):
            try:
                if parser.is_mine(pathname):
                    self.parser = parser(pathname)
            except NotSupportedVersionError:
                pass
        if self.parser is None:
            raise NotSupportedVersionError

    def get_highest_ranking(self):
        """Return the highest ranking id of the report.

        :returns: int -- the risk id of the highest ranked vulnerability
                  referenced in the report.

        .. note::

            The risk id varies from `0` (highest risk) to `n` (the lowest
            risk).

        """
        return min(
            RANKING_SCALE.get(vuln.get('ranking')) for vuln in self.vulns)

    def parse(self):
        """Abstract parser that will parse the report of a tool.

        :raises: NotImplementedError

        """
        raise NotImplementedError('The parser MUST be define for each tool.')
