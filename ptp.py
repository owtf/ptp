"""

    PTP library.

"""


from libptp.tools.skipfish.skipfish import SkipfishReport
from libptp.tools.arachni.arachni import ArachniReport
from libptp.tools.w3af.w3af import W3AFReport
import libptp.tools.skipfish.skipfish


class PTP(object):
    """PTP class definition.

    Usage:
        ptp = PTP(tool_name)
        ptp.parse(path_to_report, filename)

    """

    supported = {
        'skipfish': SkipfishReport,
        'arachni': ArachniReport,
        'w3af': W3AFReport,
        }

    def __init__(self, tool_name):
        if self._check_supported_tool(tool_name):
            self.tool_name = tool_name
        else:
            # TODO: Implement custom exception
            raise ValueError('Unsupported tool.')

    def _check_supported_tool(self, tool_name):
        return tool_name in self.supported.keys()

    def parse(self, path_to_report=None, filename=None):
        self.report = self.supported[self.tool_name]()
        return self.report.parse(path_to_report, filename)

    def get_highest_ranking(self):
        return self.report.get_highest_ranking()
