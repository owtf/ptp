"""

:synopsis: Define the basic :mod:`parser` classes that will parse the
    data from the report file.

.. moduleauthor:: Tao Sauvage

"""

import os
import fnmatch

from lxml import etree
from lxml.etree import LxmlError


class AbstractParser(object):

    """Abstract representation of a parser.

    .. note::

        This class will be extended for each pentesting tool. That way, each
        tool will add its own parsing specificities.

    """

    #: :class:`str` -- Name of the tool.
    __tool__ = None
    #: :class:`str` -- Format of reports it supports.
    __format__ = None
    #: :class:`list` -- Versions it can supports.
    __version__ = None

    def __init__(self, pathname='./', filename='*'):
        """Initialize :class:`AbstractParser`.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        #: :class:`type` -- i/o stream of the report.
        self.stream = self.handle_file(pathname, filename)
        #: :class:`list` -- List of dict of the results found in the report.
        self.vulns = []
        #: :class:`dict` -- Dict of the metadata found in the report.
        self.metadata = {}

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


    @classmethod
    def handle_file(cls, pathname='./', filename='*'):
        """Process the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        :raises: :class:`NotImplementedError` because this is an abstract
            method.

        """
        raise NotImplementedError(
            '`handle_file` function MUST be define for each parser.')

    @classmethod
    def is_mine(cls):
        """Check if it can handle the report file.

        :raises: :class:`NotImplementedError` because this is an abstract
            method.

        """
        raise NotImplementedError(
            '`is_mine` function MUST be define for each parser.')

    @classmethod
    def check_version(cls, metadata, key='version'):
        """Checks the version in the metadata against the supported one(s).

        :param dict metadata: The metadata in which to find the version.
        :param str key: The :attr:`metadata` key containing the version value.

        :return: `True` if it can parse the report, `False` otherwise.
        :rtype: :class:`bool`

        """
        if metadata[key] in cls.__version__:
            return True
        return False

    def parse_metadata(self):
        """Parse the metadata of a report.

        :raises: :class:`NotImplementedError` because this is an abstract
            method.

        """
        raise NotImplementedError(
            '`parse_metadata` function MUST be define for each parser.')

    def parse_report(self):
        """Parse the results of a report file.

        :raises: :class:`NotImplementedError` because this is an abstract
            method.

        """
        raise NotImplementedError(
            '`parse_report` function MUST be define for each parser.')


class XMLParser(AbstractParser):

    """Specialized parser for XML files.

    Define the special :func:`handle_file` function in order to process the XML
    report file.

    """

    #: str -- XMLParser only supports XML files.
    __format__ = 'xml'

    def __init__(self, pathname='./', filename='*.xml'):
        """Initialize :class:`XMLParser`.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        AbstractParser.__init__(self, pathname, filename)

    @classmethod
    def handle_file(cls, pathname='./', filename='*.xml'):
        """Return the root node of the XML file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :raises ValueError: if the report file has not the right extension.
        :raises LxmlError: if Lxml cannot parse the XML file.

        :return: handle on the root node element from the XML file.
        :rtype: :class:`lxml.etree._Element`

        """
        fullpath = cls._recursive_find(pathname, filename)
        if not len(fullpath):
            raise ValueError("No report found.")
        fullpath = fullpath[0]
        if not fullpath.endswith(cls.__format__):
            raise ValueError(
                "This parser only supports '%s' files" % cls.__format__)
        return etree.parse(fullpath).getroot()


class FileParser(AbstractParser):

    """Specialized parser for generic report file(s).

    Define the special :func:`handle_file` function in order to process the
    generic report file.

    """

    def __init__(self, pathname='./', filename='*'):
        """Initialize :class:`FileParser`.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        AbstractParser.__init__(self, pathname, filename)

    @classmethod
    def handle_file(cls, pathname='./', filename='*'):
        """Return a string of the content of the file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :raises OSError: if an error occurs when opening/reading the report
            file.
        :raises IOError: if an error occurs when opening/reading the report
            file.

        :return: all the data from the file.
        :rtype: :class:`str`

        """
        fullpath = cls._recursive_find(pathname, filename)
        if not len(fullpath):
            raise ValueError("No report found.")
        fullpath = fullpath[0]
        data = ''
        with open(fullpath, 'r') as f:
            data = f.read()
        return data


class LineParser(AbstractParser):
    """Specialized parser for generic report files.

    Define the special :func:`handle_file` function in order to process the
    generic report file.

    .. note::

        Contrary to :class:`FileParser`, this class reads the file line by line
        and return a :class:`list`, instead of a :class:`str`.

    """

    def __init__(self, pathname='./', filename='*'):
        """Initialize :class:`LineParser`.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.

        """
        AbstractParser.__init__(self, pathname, filename)

    @classmethod
    def handle_file(cls, pathname='./', filename='*', skip_empty=True):
        """Return a list of the lines of the file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool skip_empty: skip the empty lines that can occur in the
            file if `True`, otherwise keep them.
        :raises OSError: if an error occurs when opening/reading the report
            file.
        :raises IOError: if an error occurs when opening/reading the report
            file.

        :return: all the data from the file, line by line.
        :rtype: :class:`list`

        """
        fullpath = cls._recursive_find(pathname, filename)
        if not len(fullpath):
            raise ValueError("No report found.")
        fullpath = fullpath[0]
        with open(fullpath, 'r') as f:
            if skip_empty:
                return [line.rstrip('\n') for line in f.readlines() if line.rstrip('\n')]
            return [line.rstrip('\n') for line in f.readlines()]
