"""

:synopsis: Custom exceptions used across the :mod:`ptp` library.

.. moduleauthor:: Tao Sauvage

"""


class PTPError(Exception):
    """General :mod:`ptp` error."""
    pass


class ReportNotFoundError(PTPError):
    """:mod:`ptp` error when the report file(s) was not found."""
    pass


class NotSupportedToolError(PTPError):
    """:mod:`ptp` error when the tool is not supported."""
    pass


class NotSupportedVersionError(PTPError):
    """:mod:`ptp` error when the version of the tool is not supported."""
    pass
