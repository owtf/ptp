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
        ptp = PTP()
        ptp.parse(path_to_report, filename)

    """

    # Reports for supported tools.
    supported = {
        'arachni': ArachniReport,
        'skipfish': SkipfishReport,
        'w3af': W3AFReport,
        'wapiti': WapitiReport
        }

    def __init__(self, tool_name=None):
        self.tool_name = tool_name
        self.report = None

    def __str__(self):
        return self.report.__str__()

    def parse(self, pathname=None, filename=None):
        if self.tool_name is None:
            for tool in self.supported.values():
                if tool.is_mine(pathname, filename=filename):
                    print('Report matched for: ' + tool.__name__)
                    self.report = tool()
                    break
        else:
            try:
                self.report = self.supported[self.tool_name]()
            except KeyError:
                pass
        if self.report is None:
            # TODO: Implement custom exception
            raise ValueError('Unsupported tool.')
        return self.report.parse(pathname, filename)

    def get_highest_ranking(self):
        return self.report.get_highest_ranking()
