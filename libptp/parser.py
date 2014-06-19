"""

.. module:: parser
    :synopsis: The Parser class will extract the information contained in a
               report.
.. moduleauthor:: Tao Sauvage

"""


class AbstractParser(object):
    """Abstract representation of a parser."""

    __tool__ = None
    __format__ = None
    __version__ = None

    @classmethod
    def is_mine(cls, stream):
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
        raise NotImplementedError(
            "A parser MUST define the `parse_metada` method.")

    def parse_report(self, stream):
        raise NotImplementedError(
            "A parser MUST define the `parse_report` method.")
