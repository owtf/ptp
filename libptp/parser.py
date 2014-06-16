"""

    The Parser class will extract the information contained from a report.

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
        """Checks the version from the metadata against the supported one.

        The version to test is the value of metadata[key].

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
