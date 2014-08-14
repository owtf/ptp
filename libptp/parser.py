"""

:synopsis: Define the basic parser classes that will parse the data from the
    report file(s).

.. moduleauthor:: Tao Sauvage

"""


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

    def __init__(self, fullpath):
        """Initialize AbstractParser.

        :param str fullpath: full path to the report file.

        """
        #: :class:`type` -- i/o stream of the report.
        self.stream = self.handle_file(fullpath)
        #: :class:`list` -- List of dict of the results found in the report.
        self.vulns = []
        #: :class:`dict` -- Dict of the metadata found in the report.
        self.metadata = {}

    @classmethod
    def handle_file(cls, fullpath):
        """Process the report file(s) in order to create an i/o stream.

        :param str fullpath: Full path to the report file.

        :raises: :class:`NotImplementedError` because this is an abstract
            method.

        """
        raise NotImplementedError(
            '`handle_file` function MUST be define for each parser.')

    @classmethod
    def is_mine(cls, *args, **kwargs):
        """Check if the parser supports the tool.

        :param list \*args: Arguments that will be passed to the parser.
        :param dict \*\*kwargs: Arguments that will be passed to the parser.

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
        """Parse the results of a report file(s).

        :raises: :class:`NotImplementedError` because this is an abstract
            method.

        """
        raise NotImplementedError(
            '`parse_report` function MUST be define for each parser.')


class XMLParser(AbstractParser):

    """Specialized parser for XML formatted report file(s).

    Define the special :func:`handle_file` function in order to process XML
    report file(s).

    """

    #: str -- XMLParser only supports XML files.
    __format__ = 'xml'

    def __init__(self, fullpath):
        """Initialize XMLParser.

        :param str fullpath: full path to the report file.

        """
        AbstractParser.__init__(self, fullpath)

    @classmethod
    def handle_file(cls, fullpath):
        """Specialized file handler for XML files.

        :param str fullpath: path to the report file.
        :raises ValueError: if the report file has not the right extension.
        :raises LxmlError: if Lxml cannot parse the XML file.

        :return: handle on the root node element from the XML file.
        :rtype: :class:`lxml.etree._Element`

        """
        if not fullpath.endswith(cls.__format__):
            raise ValueError(
                "This parser only supports '%s' files" % cls.__format__)
        return etree.parse(fullpath).getroot()


class FileParser(AbstractParser):

    """Specialized parser for generic report file(s).

    Define the special :func:`handle_file` function in order to process generic
    report file(s).

    """

    def __init__(self, fullpath):
        """Initialize FileParser.

        :param str fullpath: full path to the report file.

        """
        AbstractParser.__init__(self, fullpath)

    @classmethod
    def handle_file(cls, fullpath):
        """Specialized file handler for generic file(s).

        :param str fullpath: full path to the report file.
        :raises OSError: if an error occurs when opening/reading the report
            file.
        :raises IOError: if an error occurs when opening/reading the report
            file.

        :return: string containing all the data from the file.
        :rtype: :class:`str`

        """
        data = ''
        with open(fullpath, 'r') as f:
            data = f.read()
        return data


class LineParser(AbstractParser):
    """Specialized parser for generic report file(s).

    Define the special :func:`handle_file` function in order to process generic
    report file(s).

    .. note::

        Contrary to :class:`FileParser`, this class reads the file line by line
        and generates a list, instead of a string.

    """

    def __init__(self, fullpath):
        """Initialize LineParser.

        :param str fullpath: full path to the report file.

        """
        AbstractParser.__init__(self, fullpath)

    @classmethod
    def handle_file(cls, fullpath, skip_empty=True):
        """Specialized file handler for general files read line by line.

        :param str fullpath: path to the report file.
        :param bool skip_empty: skip the empty lines that can occur in the
            file if `True`, otherwise keep them.
        :raises OSError: if an error occurs when opening/reading the report
            file.
        :raises IOError: if an error occurs when opening/reading the report
            file.

        :return: list of strings containing all the data from the file, line
            by line.
        :rtype: :class:`str`

        """
        with open(fullpath, 'r') as f:
            if skip_empty:
                return [line.rstrip('\n') for line in f.readlines() if line.rstrip('\n')]
            return [line.rstrip('\n') for line in f.readlines()]
