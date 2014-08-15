"""

:synopsis: :mod:`ptp` library entry point that exposes the public API.

.. moduleauthor:: Tao Sauvage

"""

from .libptp.exceptions import NotSupportedToolError, NotSupportedVersionError
from .libptp.constants import UNKNOWN, RANKING_SCALE
from .tools.arachni.parser import ArachniXMLParser
from .tools.skipfish.parser import SkipfishJSParser
from .tools.w3af.parser import W3AFXMLParser
from .tools.wapiti.parser import WapitiXMLParser, Wapiti221XMLParser
from .tools.metasploit.parser import MetasploitParser
from .tools.dirbuster.parser import DirbusterParser
from .tools.nmap.parser import NmapXMLParser
from .tools.owasp.cm008.parser import OWASPCM008Parser
from .tools.robots.parser import RobotsParser


class PTP(object):

    """:class:`PTP` class exposing :mod:`ptp`'s public API.

    Example::

        ptp = PTP(pathname='my/path')
        ptp.parse()

    """

    #: :class:`dict` -- Supported tools and their parser(s).
    supported = {
        'arachni': [ArachniXMLParser],
        'skipfish': [SkipfishJSParser],
        'w3af': [W3AFXMLParser],
        'wapiti': [WapitiXMLParser, Wapiti221XMLParser],
        'metasploit': [MetasploitParser],
        'dirbuster': [DirbusterParser],
        'nmap': [NmapXMLParser],
        'owasp-cm-008': [OWASPCM008Parser],
        'robots': [RobotsParser]}

    def __init__(self, tool_name='', *args, **kwargs):
        """Initialize :class:`PTP`.

        :param str tool_name: help :mod:`ptp` by specifying the name of the
            tool that has generated the target report.
        :param list \*args: Arguments that are needed by the parser.
        :param dict \*\*kwargs: Arguments that are needed by the parser.

        """
        #: :class:`str` -- Name of the tool that generated the report.
        self.tool_name = tool_name
        #: :class:`libptp.AbstractParser` -- Parser used on the report.
        self.parser = None
        #: :class:`list` -- Vulnerabilities that are listed in the report.
        self.vulns = []
        #: :class:`dict` -- Metadata from the report.
        self.metadata = {}
        if args or kwargs:
            self._init_parser(*args, **kwargs)

    def _init_parser(self, *args, **kwargs):
        """Find and initialize the parser.

        :param str tool_name: help PTP by specifying the name of the tool that
            has generated the target report.
        :param list \*args: Arguments that are needed by the parser.
        :param dict \*\*kwargs: Arguments that are needed by the parser.

        """
        if not self.tool_name:
            # Since no tool name has been specified by the user, try to
            # automatically detect it.
            try:
                supported = self.supported.itervalues()
            except AttributeError:  # Python3 then.
                supported = self.supported.values()
        else:
            supported = [self.supported.get(self.tool_name)]
        supported = [parser for parsers in supported for parser in parsers]

        for parser in supported:
            try:
                if parser.is_mine(*args, **kwargs):
                    self.parser = parser
                    break
            except TypeError:
                pass
            except NotSupportedVersionError:
                pass
        # Check if instanciated.
        if self.parser and not hasattr(self.parser, 'stream'):
            self.parser = self.parser(*args, **kwargs)

    def parse(self, *args, **kwargs):
        """Parse a tool report.

        :param list \*args: Arguments that are needed by the parser.
        :param dict \*\*kwargs: Arguments that are needed by the parser.
        :raises NotSupportedToolError: if the tool that has generated the
            report is not supported by PTP.

        :return: The list of dictionaries of the results found in the report.
        :rtype: :class:`list`

        """
        if self.parser is None:
            self._init_parser(*args, **kwargs)
        if self.parser is None:
            raise NotSupportedToolError('This tool is not supported by PTP.')
        # Instantiate the report class.
        self.tool_name = self.parser.__tool__
        self.metadata = self.parser.parse_metadata()
        self.vulns = self.parser.parse_report()
        return self.vulns

    def get_highest_ranking(self):
        """Return the highest ranking of the report.

        :return: the risk id of the highest ranked vulnerability referenced in
            the report.
        :rtype: :class:`int`

        .. note::

            The ranking starts from `0` to `n` where `n` represents the most
            critical risk. (See :mod:`libptp.constants`).

        """
        if not self.vulns:
            return UNKNOWN
        return max(
            RANKING_SCALE.get(vuln.get('ranking')) for vuln in self.vulns)
