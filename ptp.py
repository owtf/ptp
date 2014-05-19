"""

    PTP library.

"""


from libptp.tools.skipfish.skipfish import SkipfishReport
import libptp.tools.skipfish.skipfish


class PTP(object):
    """PTP class definition.

    Usage:
        ptp = PTP(tool_name)
        ptp.parse(path_to_report)

    """

    supported = {
        'skipfish': SkipfishReport,
        }

    def __init__(self, tool_name):
        if self._check_supported_tool(tool_name):
            self.tool_name = tool_name
        else:
            # TODO: Implement custom exception
            raise ValueError('Unsupported tool.')

    def _check_supported_tool(self, tool_name):
        return tool_name in self.supported.keys()

    def parse(self, path_to_report):
        self.report = self.suported[self.tool_name](path_to_report)
        return self.report.parse()

    def get_highest_ranking(self):
        return self.report.get_highest_ranking()
