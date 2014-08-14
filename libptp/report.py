"""

:synopsis: Define the basic report classes that will represent the data from
    the report file(s).

.. moduleauthor:: Tao Sauvage

"""


import os
import fnmatch

from libptp.exceptions import NotSupportedVersionError
from libptp.constants import UNKNOWN, RANKING_SCALE


class AbstractReport(object):

    """Abstract representation of a report provided by a pentesting tool.

    .. note::

        This class will be extended for each pentesting tool. That way, each
        tool will add its own reporting specificities.

    """

    #: :class:`str` -- Name of the tool that has generated the report file(s).
    __tool__ = None
    #: :class:`list` -- Available parsers for the tool.
    __parsers__ = None

    def __init__(self):
        """Initialized the AbstractReport instance."""
        #: :class:`AbstractParser` -- The current parser the report is using.
        self.parser = None
        #: :class:`list` -- List of dict of the results found in the report.
        self.vulns = []

    @classmethod
    def is_mine(cls, parsers, pathname=None, filename=None):
        """Check if the report can parse the report.

        :param :class:`libptp.parser.AbstractParser` parsers: List of the
            available parsers for the report.
        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        if pathname is None or filename is None:
            return False
        fullpath = cls._recursive_find(pathname, filename)
        if not fullpath:
            return False
        fullpath = fullpath[0]  # Only keep the first file.
        return AbstractReport._is_parser(parsers, fullpath)

    @classmethod
    def _is_parser(cls, parsers, *args, **kwargs):
        """Check if a parser exists for that report.

        :param list parsers: The available parsers of this class.
        :param list \*args: Arguments that will be pass to the parser.
        :param dict \*\*kwargs: Arguments that will be pass to the parser.

        :return: `True` if this class has a parser for this tool, `False`
            otherwise.
        :rtype: :class:`bool`

        """
        if parsers is not None:
            for parser in parsers:
                if parser.is_mine(*args, **kwargs):
                    return True
        return False

    @staticmethod
    def _recursive_find(pathname='./', file_regex='*', early_break=True):
        """Retrieve the full path to the report file(s).

        :param str pathname: The root directory where to start searching.
        :param re file_regex: The regex that will be matched against all files
            from within `pathname`.
        :param bool early_break: Stop the search as soon as a file has been
            matched.

        :return: A list of path to the matched files that have been found.
        :rtype: :class:`list`

        .. note::

            The search occurs starting from `pathname` as the root directory.

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

    def _init_parser(self, *args, **kwargs):
        """Instantiate the correct parser for the report.

        :param list args: Arguments that will be passed to the parser.
        :param dict kwargs: Arguments that will be passed to the parser.

        :raises: :class:`NotSupportedVersionError` -- if it does not support
            that version of the tool.

        """
        for parser in self.__parsers__:
            try:
                if parser.is_mine(*args, **kwargs):
                    self.parser = parser(*args, **kwargs)
            except TypeError:
                pass
            except NotSupportedVersionError:
                pass
        if self.parser is None:
            raise NotSupportedVersionError

    def get_highest_ranking(self):
        """Return the highest ranking value of the report.

        :return: the risk id of the highest ranked vulnerability
            referenced in the report.
        :rtype: :class:`int`

        .. note::

            The rank value starts from `0` to `n` where `n` represents the
            most critical risk.

        """
        if not self.vulns:
            return UNKNOWN
        return max(
            RANKING_SCALE.get(vuln.get('ranking')) for vuln in self.vulns)

    def parse(self):
        """Proxy call to the parser's parse function.

        :raises: :class:`NotImplementedError` -- because this is an abstract
            method.

        """
        raise NotImplementedError(
            '`parse` function MUST be define for each parser.')
