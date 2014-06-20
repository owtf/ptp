"""

.. module:: parser
    :synopsis: The Parser class will extract the information contained in a
               report.

.. moduleauthor:: Tao Sauvage

"""


from lxml import etree
from lxml.etree import LxmlError


class AbstractParser(object):
    """Abstract representation of a parser."""

    #: str -- Name of the tool.
    __tool__ = None
    #: str -- Format of reports it supports.
    __format__ = None
    #: list -- Versions it can supports.
    __version__ = None

    def __init__(self, pathname):
        """Initialize AbstractParser.

        :param pathname: path to the report file.
        :type pathname: str.

        """
        #: i/o stream -- i/o stream of the report.
        self.stream = self.handle_file(pathname)

    @classmethod
    def handle_file(cls, pathname):
        """Process the report file(s) in order to create an i/o stream.

        :param pathname: Path to the report file.
        :type pathname: str.
        :raises: NotImplementedError

        """
        raise NotImplementedError(
            "A parser MUST define the `handle_file` method.")

    @classmethod
    def is_mine(cls, *args, **kwargs):
        """Check if the parser supports the tool.

        :param pathname: Path to the report file.
        :type pathname: str.
        :raises: NotImplementedError

        """
        raise NotImplementedError("A parser MUST define the `is_mine` method.")

    @classmethod
    def check_version(cls, metadata, key='version'):
        """Checks the version in the metadata against the supported one.

        :param metadata: The metadata in which to find the version.
        :type metadata: dict.
        :param key: The :attr:`metadata` key containing the version value.
        :type key: str.

        :returns: bool -- `True` if it can parse the report, `False` otherwise.

        """
        if metadata[key] in cls.__version__:
            return True
        return False

    def parse_metadata(self):
        """Parse the metadata of a report.

        :raises: NotImplementedError

        """
        raise NotImplementedError(
            "A parser MUST define the `parse_metadata` method.")

    def parse_report(self):
        """Parse the discoveries of a report.

        :raises: NotImplementedError

        """
        raise NotImplementedError(
            "A parser MUST define the `parse_report` method.")


class XMLParser(AbstractParser):
    """Specialized parser for XML formatted report."""

    #: str -- XMLParser only supports XML files.
    __format__ = 'xml'

    def __init__(self, pathname):
        """Initialize XMLParser.

        :param pathname: path to the report file.
        :type pathname: str.

        """
        AbstractParser.__init__(self, pathname)

    @classmethod
    def handle_file(cls, pathname):
        """Specialized file handler for XML files.

        :param pathname: path to the report file.
        :type pathname: str.
        :raises: ValueError, LmxlError

        """
        if not pathname.endswith(cls.__format__):
            raise ValueError(
                "This parser only supports '%s' files" % self.__format__)
        return etree.parse(pathname).getroot()
