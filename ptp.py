"""

.. module:: ptp
    :synopsis: PTP library.

.. moduleauthor:: Tao Sauvage

"""


from libptp.exceptions import NotSupportedToolError
from libptp.tools.arachni.report import ArachniReport
from libptp.tools.skipfish.report import SkipfishReport
from libptp.tools.w3af.report import W3AFReport
from libptp.tools.wapiti.report import WapitiReport


class PTP(object):

    """PTP class definition aiming to help users to use `libptp`.

    Example::

        ptp = PTP()
        ptp.parse(path_to_report)

    """

    #: Dictionary linking the tools to their report classes.
    supported = {
        'arachni': ArachniReport,
        'skipfish': SkipfishReport,
        'w3af': W3AFReport,
        'wapiti': WapitiReport,}

    def __init__(self, tool_name=None):
        self.tool_name = tool_name
        self.report = None

    def __str__(self):
        return self.report.__str__()

    def parse(self, pathname=None):
        """Parse a tool report.

        :param pathname: The path to the report.
        :type pathname: str.
        :raises: NotSupportedToolError

        :returns: list -- The list of dictionaries of the results found in the
                  report.

        """
        if self.tool_name is None:
            try:
                supported = self.supported.itervalues()
            except AttributeError:  # Python3 then.
                supported = self.supported.values()
            for tool in supported:
                if tool.is_mine(pathname):
                    self.report = tool
                    break
        else:
            self.report = self.supported.get(self.tool_name)
        if self.report is None:
            raise NotSupportedToolError('This tool is not supported by PTP.')
        self.report = self.report()  # Instantiate the report class.
        return self.report.parse(pathname)

    def get_highest_ranking(self):
        """Retrieve the highest ranked vulnerability level from the report.

        :returns: int -- The highest ranked vulnerability level.

        .. note::

            The `level` starts from `0` to `n` where `0` represents the highest
            risk.

        """
        if self.report:
            return self.report.get_highest_ranking()
        return None
