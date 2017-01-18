"""

:synopsis: Define the basic :mod:`parser` classes that will parse the data from the report file.

.. moduleauthor:: Tao Sauvage

"""

import os
import re
import fnmatch

import json
from lxml import etree


class AbstractParser(object):

    """Abstract representation of a parser.

    .. note::

        This class will be extended for each pentesting tool. That way, each tool will add its own parsing
        specificities.

    """

    #: :class:`str` -- Name of the tool.
    __tool__ = None
    #: :class:`str` -- Format of reports it supports.
    __format__ = None
    #: :class:`list` -- Versions it can supports.
    __version__ = ''

    def __init__(self, pathname='./', filename='*', light=False, first=True):
        """Initialize :class:`AbstractParser`.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool light: `True` to only parse the ranking of the findings from the report.
        :param bool first: Only process first file (``True``) or each file that matched (``False``).

        """
        #: :class:`str` -- Path to the report directory.
        self.pathname = pathname
        #: :class:`type` -- i/o stream of the report.
        self.stream = self.handle_file(pathname, filename, first=first)
        #: :class:`list` -- List of dict of the results found in the report.
        self.vulns = []
        #: :class:`dict` -- Dict of the metadata found in the report.
        self.metadata = {}
        #: :class:`bool` -- Should fully parse the report or not.
        self.light = light

    @staticmethod
    def _recursive_find(pathname='./', file_regex='*', first=True):
        """Retrieve the full path to the report file(s).

        :param str pathname: The root directory where to start searching.
        :param re file_regex: The regex that will be matched against all files from within `pathname`.
        :param bool first: Stop the search as soon as a file has been matched.

        :return: A list of path to the matched files that have been found.
        :rtype: list

        .. note::

            The search occurs starting from `pathname` as the root directory.

        """
        founds = []
        for base, _, files in os.walk(pathname):
            try:
                is_str = isinstance(files, basestring)  # Python 2.x.
            except NameError:
                is_str = isinstance(files, str)  # Python 3.x.
            if is_str and fnmatch.fnmatch(files, file_regex):  # Only one file has been found (str).
                founds.append(os.path.join(base, files))
            else:  # Several files have been found (list).
                matched_files = fnmatch.filter(files, file_regex)
                founds.extend(os.path.join(base, matched_file) for matched_file in matched_files)
            if founds and first:
                founds = [founds[0]]
                break
        return founds

    @classmethod
    def handle_file(cls, pathname='./', filename='*', first=True):
        """Process the report file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Stop the search as soon as a file has been matched.

        :raises: :class:`NotImplementedError` because this is an abstract method.

        """
        raise NotImplementedError('`handle_file` function MUST be defined for each parser.')

    @classmethod
    def is_mine(cls):
        """Check if it can handle the report file.

        :raises: :class:`NotImplementedError` because this is an abstract method.

        """
        raise NotImplementedError('`is_mine` function MUST be defined for each parser.')

    @classmethod
    def check_version(cls, metadata, key='version'):
        """Checks the version in the metadata against the supported one(s).

        :param dict metadata: The metadata in which to find the version.
        :param str key: The :attr:`metadata` key containing the version value.

        :return: `True` if it can parse the report, `False` otherwise.
        :rtype: bool

        """
        try:
            # Is there a non-empty result from re.findall?
            if list(filter(None, re.findall(cls.__version__, metadata[key], re.IGNORECASE))):
                return True
        except KeyError:
            pass
        return False

    def parse_metadata(self):
        """Parse the metadata of a report.

        :raises: NotImplementedError because this is an abstract method.

        """
        raise NotImplementedError('`parse_metadata` function MUST be defined for each parser.')

    def parse_report(self):
        """Parse the results of a report file.

        :raises: NotImplementedError because this is an abstract method.

        """
        raise NotImplementedError('`parse_report` function MUST be defined for each parser.')


class XMLParser(AbstractParser):

    """Specialized parser for XML files.

    Define the special :func:`handle_file` function in order to process the XML report file.

    """

    #: str -- XMLParser only supports XML files.
    __format__ = 'xml'

    def __init__(self, pathname='./', filename='*.xml', **kwargs):
        """Initialize :class:`XMLParser`."""
        AbstractParser.__init__(self, pathname, filename, **kwargs)

    @classmethod
    def handle_file(cls, pathname='./', filename='*.xml', first=True):
        """Return the root node of the XML file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Stop the search as soon as a file has been matched.

        :raises IOError: when the report file cannot be found.
        :raises TypeError: when the report file has not the right extension.
        :raises lxml.etree.XMLSyntaxError: when Lxml cannot parse the XML file.

        :return: handle on the root node element from the XML file.
        :rtype: :class:`lxml.etree._Element`

        """
        fullpath = cls._recursive_find(pathname, filename, first=first)
        if not len(fullpath):
            raise IOError("Report matching '%s' cannot be found." % os.path.join(pathname, filename))
        fullpath = fullpath[0]
        if not fullpath.endswith(cls.__format__):
            raise TypeError("This parser only supports '%s' files" % cls.__format__)
        return etree.parse(fullpath).getroot()


class FileParser(AbstractParser):

    """Specialized parser for generic report file(s).

    Define the special :func:`handle_file` function in order to process the generic report file.

    """

    @classmethod
    def handle_file(cls, pathname='./', filename='*', first=True):
        """Return a string of the content of the file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Stop the search as soon as a file has been matched.

        :raises IOError: when the report file cannot be found or an error occurs when opening/reading.
        :raises OSError: when an error occurs when opening/reading the report file.

        :return: data from the file.
        :rtype: str

        """
        fullpath = cls._recursive_find(pathname, filename, first=first)
        if not len(fullpath):
            raise IOError("Report matching '%s' cannot be found." % filename)
        fullpath = fullpath[0]
        data = ''
        with open(fullpath, 'r') as f:
            data = f.read()
        return data


class LineParser(AbstractParser):

    """Specialized parser for generic report files.

    Define the special :func:`handle_file` function in order to process the generic report file.

    .. note::

        Contrary to :class:`FileParser`, this class reads the file line by line and return a :class:`list`, instead of
        a :class:`str`.

    """

    @classmethod
    def handle_file(cls, pathname='./', filename='*', skip_empty=True, first=True):
        """Return a list of the lines of the file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Stop the search as soon as a file has been matched.
        :param bool skip_empty: skip the empty lines that can occur in the file if `True`, otherwise keep them.

        :raises IOError: when the report file cannot be found or an error occurs when opening/reading.
        :raises OSError: when an error occurs when opening/reading the report file.

        :return: all the data from the file, line by line.
        :rtype: list

        """
        fullpath = cls._recursive_find(pathname, filename, first=first)
        if not len(fullpath):
            raise IOError("Report matching '%s' cannot be found." % filename)
        data = []
        for current_file in fullpath:
            with open(current_file, 'r') as f:
                if skip_empty:
                    data.extend([line.rstrip('\n\r') for line in f.readlines() if line.rstrip('\n\r')])
                else:
                    data.extend([line.rstrip('\n\r') for line in f.readlines()])
        return data


class JSONParser(AbstractParser):

    """Specialized parser for JSON files.

    Define the special :func:`handle_file` function in order to process the JSON report file.

    """

    #: str -- JSONParser only supports json files.
    __format__ = 'json'

    @classmethod
    def handle_file(cls, pathname='./', filename='*.json', first=True):
        """Return the dict of the JSON file.

        :param str pathname: Path to the report directory.
        :param str filename: Regex matching the report file.
        :param bool first: Stop the search as soon as a file has been matched.

        :raises IOError: when the report file cannot be found.
        :raises TypeError: when the report file has not the right extension.
        :raises ValueError: when json cannot parse the JSON file.

        """
        fullpath = cls._recursive_find(pathname, filename, first=first)
        if not len(fullpath):
            raise IOError("Report matching '%s' cannot be found." % filename)
        fullpath = fullpath[0]
        if not fullpath.endswith(cls.__format__):
            raise TypeError("This parser only supports '%s' files" % cls.__format__)
        with open(fullpath, 'r') as data:
            return json.load(data)
