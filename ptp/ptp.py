"""

:synopsis: :mod:`ptp` library entry point that exposes the public API.

.. moduleauthor:: Tao Sauvage

"""

from .libptp.exceptions import NotSupportedToolError, NotSupportedVersionError
from .libptp.constants import UNKNOWN, RANKING_SCALE
from .tools.arachni.parser import ArachniXMLParser, ArachniJSONParser
from .tools.skipfish.parser import SkipfishJSParser
from .tools.w3af.parser import W3AFXMLParser
from .tools.wapiti.parser import WapitiXMLParser, Wapiti221XMLParser
from .tools.metasploit.parser import MetasploitParser
from .tools.dirbuster.parser import DirbusterParser
from .tools.nmap.parser import NmapXMLParser
from .tools.owasp.cm008.parser import OWASPCM008Parser
from .tools.robots.parser import RobotsParser
from .tools.burpsuite.parser import BurpXMLParser


class PTP(object):

    """:class:`PTP` class exposing :mod:`ptp`'s public API.

    Example::

        ptp = PTP(pathname='my/path')
        ptp.parse()

    """

    #: :class:`dict` -- Supported tools and their parser(s).
    supported = {
        'arachni': [ArachniXMLParser, ArachniJSONParser],
        'skipfish': [SkipfishJSParser],
        'w3af': [W3AFXMLParser],
        'wapiti': [WapitiXMLParser, Wapiti221XMLParser],
        'metasploit': [MetasploitParser],
        'dirbuster': [DirbusterParser],
        'nmap': [NmapXMLParser],
        'owasp-cm-008': [OWASPCM008Parser],
        'robots': [RobotsParser],
        'burpsuite': [BurpXMLParser]}

    def __init__(self, tool_name='', cumulative=False):
        """Initialize :class:`PTP`.

        :param str tool_name: help :mod:`ptp` by specifying the name of the tool that has generated the target report.
        :param bool cumulative: `True` to cumulate the vulns across multiple tools. `False` to reset them.

        :raises: :class:`ptp.libptp.exceptions.NotSupportedToolError` when ``tool_name`` is not in the PTP's supported
            tools list.

        """
        if tool_name and tool_name not in self.supported:
            raise NotSupportedToolError("The tool '%s' is not supported by PTP." % tool_name)
        #: :class:`str` -- Name of the tool that generated the report.
        self.tool_name = tool_name
        #: :class:`libptp.AbstractParser` -- Parser used on the report.
        self._parser = None
        #: :class:`list` -- Vulnerabilities that are listed in the report.
        self.vulns = []
        #: :class:`dict` -- Metadata from the report.
        self.metadata = {}
        #: :class:`bool` -- Check if user wants vulns to be re-intialised for each run ot not.
        self.cumulative = cumulative
        # Parser was chosen automatically.
        self._auto = True

    def _init_parser(self, *args, **kwargs):
        """Find and initialize the parser automatically.

        :param list \*args: Arguments that are needed by the parser.
        :param dict \*\*kwargs: Arguments that are needed by the parser.

        """
        if self._auto:
            if not self.tool_name:
                # Since no tool name has been specified by the user, try all parsers.
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
                        self._parser = parser
                        break
                except TypeError:  # Mismatch in terms of arguments, therefore must not be the correct parser.
                    pass
                except NotSupportedVersionError:  # Mismatch in terms of supported version.
                    pass
                except (IOError, OSError):  # Mismatch in terms of report files.
                    pass
        # Check if instantiated.
        if self._parser and not hasattr(self._parser, 'stream'):
            self._parser = self._parser(*args, **kwargs)

    def parse(self, *args, **kwargs):
        """Parse a tool report.

        :param list \*args: Arguments that are needed by the parser.
        :param dict \*\*kwargs: Arguments that are needed by the parser.

        :raises: :class:`NotSupportedToolError` if the tool that has generated the report is not supported by PTP.

        :return: The list of dictionaries of the results found in the report.
        :rtype: list

        """
        # Ensure that parser is properly initialized.
        self._init_parser(*args, **kwargs)
        # PTP could not automatically detect the parser or manually initialize it.
        if self._parser is None:
            raise NotSupportedToolError('This tool is not supported by PTP. No parser matched `ToolParser(%s, %s)`\n\n' % (args, kwargs))

        self.tool_name = self._parser.__tool__
        self.metadata = self._parser.parse_metadata()
        if self.cumulative:
            self.vulns.extend(self._parser.parse_report())
        else:
            self.vulns = self._parser.parse_report()
        return self.vulns

    @property
    def highest_ranking(self):
        """Return the highest ranking of the report.

        :return: the risk id of the highest ranked vulnerability referenced in the report.
        :rtype: int

        .. note::

            The ranking starts from `0` to `n` where `n` represents the most critical risk.
            (See :mod:`ptp.libptp.constants`).

        """
        if not self.vulns:
            return UNKNOWN
        return max(RANKING_SCALE.get(vuln.get('ranking'), UNKNOWN) for vuln in self.vulns)

    @property
    def parser(self):
        return self._parser

    @parser.setter
    def parser(self, parser):
        """Set the parser that will be used by PTP, while keeping internal state consistent."""
        self._auto = False  # Manual mode
        self._parser = parser
