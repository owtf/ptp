"""

.. module:: parser
    :synopsis: The Parser class will extract the information contained in a
               report.

.. moduleauthor:: Tao Sauvage

"""


class AbstractParser(object):
    """Abstract representation of a parser."""

    #: str -- Name of the tool.
    __tool__ = None
    #: str -- Format of reports it supports.
    __format__ = None
    #: list -- Versions it can supports.
    __version__ = None

    @classmethod
    def is_mine(cls, stream):
        """Check if the parser supports the tool.

        :raises: NotImplementedError

        :returns: bool -- `True` if it supports this tool, `False` otherwise.

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

    def parse_metadata(self, stream):
        """Parse the metadata of a report.

        :param stream: i/o stream of the content of the report.
        :type stream: i/o stream.
        :raises: NotImplementedError

        """
        raise NotImplementedError(
            "A parser MUST define the `parse_metadata` method.")

    def parse_report(self, stream):
        """Parse the discoveries of a report.

        :param stream: i/o stream of the content of the report.
        :type stream: i/o stream.
        :raises: NotImplementedError

        """
        raise NotImplementedError(
            "A parser MUST define the `parse_report` method.")
