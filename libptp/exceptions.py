"""

:synopsis: Custom exceptions used across the :mod:`ptp` library.

.. moduleauthor:: Tao Sauvage

"""


class PTPError(Exception):
    """General PTP error."""
    pass


class ReportNotFoundError(PTPError):
    """PTP error raised when the report file(s) was not found."""
    pass


class NotSupportedToolError(PTPError):
    """PTP error raised when the tool is not supported"""
    pass


class NotSupportedVersionError(PTPError):
    """PTP error raised when the version of the tool is not supported"""
    pass
