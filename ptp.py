"""

:synopsis: PTP library entry point that exposes the public available functions.

.. moduleauthor:: Tao Sauvage

"""


from libptp.exceptions import NotSupportedToolError
from libptp.constants import UNKNOWN
from libptp.tools.arachni.report import ArachniReport
from libptp.tools.skipfish.report import SkipfishReport
from libptp.tools.w3af.report import W3AFReport
from libptp.tools.wapiti.report import WapitiReport
from libptp.tools.metasploit.report import MetasploitReport
from libptp.tools.dirbuster.report import DirbusterReport
from libptp.tools.nmap.report import NmapReport
from libptp.tools.owasp.cm008.report import OWASPCM008Report
from libptp.tools.robots.report import RobotsReport


class PTP(object):

    """PTP class exposing the PTP's public API.

    Example::

        ptp = PTP()
        ptp.parse(path_to_report)

    """

    #: :class:`dict` -- Dict linking the supported tools with their reports.
    supported = {
        'arachni': ArachniReport,
        'skipfish': SkipfishReport,
        'w3af': W3AFReport,
        'wapiti': WapitiReport,
        'metasploit': MetasploitReport,
        'dirbuster': DirbusterReport,
        'nmap': NmapReport,
        'owasp-cm-008': OWASPCM008Report,
        'robots': RobotsReport}

    def __init__(self, tool_name=''):
        """Initialize a PTP instance.

        :param str tool_name: help PTP by specifying the name of the tool that
            has generated the target report.

        """
        self.tool_name = tool_name
        self.report = None

    def parse(self, *args, **kwargs):
        """Parse a tool report.

        :param list \*args: List of arguments that are needed by the specific
            report.
        :param dict \*\*kwargs: Dict of arguments that are needed by the
            specific report.
        :raises NotSupportedToolError: if the tool that has generated the
            report is not supported by PTP.

        :return: The list of dictionaries of the results found in the report.
        :rtype: :class:`list`

        """
        if not self.tool_name:
            # Since no tool name has been specified by the user, try to
            # automatically detect it.
            try:
                supported = self.supported.itervalues()
            except AttributeError:  # Python3 then.
                supported = self.supported.values()
            for tool in supported:
                try:
                    if tool.is_mine(*args, **kwargs):
                        self.report = tool
                        break
                except TypeError:
                    pass
        else:
            self.report = self.supported.get(self.tool_name)
        if self.report is None:
            raise NotSupportedToolError('This tool is not supported by PTP.')
        self.report = self.report()  # Instantiate the report class.
        return self.report.parse(*args, **kwargs)

    def get_highest_ranking(self):
        """Retrieve the rank of the most critical discovery.

        :return: The most critical rank value.
        :rtype: :class:`int`

        .. note::

            The rank value starts from `0` to `n` where `n` represents the
            most critical risk.

        """
        if self.report:
            return self.report.get_highest_ranking()
        return UNKNOWN
