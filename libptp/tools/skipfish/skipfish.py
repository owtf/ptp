from __future__ import print_function

import os
import re
import ast

from libptp import constants
from libptp.info import Info
from libptp.report import AbstractReport


class SkipfishReport(AbstractReport):
    """Retrieve the information of a skipfish report."""

    __version__ = ['2.10b']
    __reportfile__ = 'samples.js'
    __metadatafile__ = 'summary.js'

    HIGH = 4
    MEDIUM = 3
    LOW = 2
    WARNINGS = 1
    INFO = 0

    RANKING_SCALE = {
        HIGH: constants.HIGH,
        MEDIUM: constants.MEDIUM,
        LOW: constants.LOW,
        WARNINGS: constants.INFO,
        INFO: constants.INFO}

    def __init__(self, *args, **kwargs):
        self.re_metadata = re.compile(
            r"var\s+([a-zA-Z_0-9]+)\s+=\s+'{0,1}([^;']*)'{0,1};")
        self.re_report = re.compile(
            r"var\s+([a-zA-Z_0-9]+)\s+=\s+([^;]*);")
        AbstractReport.__init__(self, *args, **kwargs)
        self.vulns = []

    def parse(self, path_to_report):
        """Parse a skipfish resport."""
        if (path_to_report is None or not os.path.isdir(path_to_report)):
            print('A directory to the report must be specified.')
            return
        self.directory = path_to_report
        self.parse_metadata()
        self.parse_report()
        # TODO: Return somethin like an unified version of the report.

    def _check_version(self, metadata):
        """Checks the version from the metadata to the supported one."""
        if metadata['sf_version'] in self.__version__:
            return True
        return False

    def parse_metadata(self):
        """Retrieve the metadata of the report.

        In skipfish the metadata are saved into the summary.js file as follow:
            var sf_version = version<string>;
            var scan_date  = date<'Ddd Mmm d hh:mm:ss yyyy'>;
            var scan_seed  = scan seed<integer>
            var scan_ms    = elapsed time in ms<integer>;

        """
        with open(os.path.join(self.directory, self.__metadatafile__), 'r') as f:
            re_result = self.re_metadata.findall(f.read())
            metadata = dict({el[0]: el[1] for el in re_result})
            # Check if the version if the good one
            if self._check_version(metadata):
                self.metadata = metadata
            else:
                # TODO: Implement custom exception
                raise ValueError(
                    'PTP does NOT support this version of Skipfish.')

    def parse_report(self):
        """Retrieve the results from the report.

        Example of the structure:
        [{ 'severity': 3, 'type': 40402, 'samples': [
            { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/0' },
            { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/1' },
            { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/2' } ]
        },]

        """
        REPORT_VAR_NAME = 'issue_samples'
        with open(os.path.join(self.directory, self.__reportfile__), 'r') as f:
            re_result = self.re_report.findall(f.read())
            report = dict({el[0]: el[1] for el in re_result})
            if not REPORT_VAR_NAME in report:
                # TODO: Implement custom exception
                raise ValueError(
                    'PTP did NOT find issue_samples variable. Is this the '
                    'right file?')
            # We now have a raw version of the Skipfish report as a list of
            # dict.
            self.raw_report = ast.literal_eval(report[REPORT_VAR_NAME])
        self._convert_report()

    def _convert_report(self):
        """Convert a Skipfsih report to a list of Info.

        Retrieve the following attributes:
            + severity

        """
        for vuln in self.raw_report:
            info = Info(
                # Convert the severity of the issue thanks to an unified
                # ranking scale.
                ranking=self.RANKING_SCALE[vuln['severity']]
                )
            self.vulns.append(info)
