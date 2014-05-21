"""

    PTP library.

"""


from libptp.tools.arachni.arachni import ArachniReport
from libptp.tools.skipfish.skipfish import SkipfishReport
from libptp.tools.w3af.w3af import W3AFReport
from libptp.tools.wapiti.wapiti import WapitiReport


class PTP(object):
    """PTP class definition.

    Usage:
        ptp = PTP(tool_name)
        ptp.parse(path_to_report, filename)

    """

    # Reports for supported tools.
    supported = (
        ArachniReport,
        SkipfishReport,
        W3AFReport,
        WapitiReport
        )

    def __init__(self):
        self.report = None

    def parse(self, pathname=None, filename=None):
        for tool in self.supported:
            if tool.is_mine(pathname, filename=filename):
                print('Report matched for: ' + tool.__name__)
                self.report = tool()
                break
        if self.report is None:
            # TODO: Implement custom exception
            raise ValueError('Unsupported tool.')
        return self.report.parse(pathname, filename)

    def get_highest_ranking(self):
        return self.report.get_highest_ranking()
