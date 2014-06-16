import re
import ast

from libptp.exceptions import NotSupportedVersionError
from libptp.info import Info
from libptp.parser import AbstractParser


class SkipfishJSONParser(AbstractParser):

    __tool__ = 'skipfish'
    __format__ = 'json'
    __version__ = ['2.10b']

    def __init__(self, *args, **kwargs):
        AbstractParser.__init__(self, *args, **kwargs)
        self.re_metadata = re.compile(
            r"var\s+([a-zA-Z_0-9]+)\s+=\s+'{0,1}([^;']*)'{0,1};")
        self.re_report = re.compile(
            r"var\s+([a-zA-Z_0-9]+)\s+=\s+([^;]*);")

    # FIXME: Find a nice way to check for a correct parser.
    @classmethod
    def is_mine(cls, stream):
        return True

    def parse_metadata(self, stream):
        """Retrieve the metadata of the report.

        In skipfish the metadata are saved into the summary.js file as follow:
            var sf_version = version<string>;
            var scan_date  = date<'Ddd Mmm d hh:mm:ss yyyy'>;
            var scan_seed  = scan seed<integer>
            var scan_ms    = elapsed time in ms<integer>;

        """
        re_result = self.re_metadata.findall(stream)
        metadata = dict({el[0]: el[1] for el in re_result})
        # Check if the version if the good one
        if self.check_version(metadata, key='sf_version'):
            return metadata
        else:
            raise NotSupportedVersionError(
                'PTP does NOT support this version of ' +
                self.__tool__ + '.')

    def parse_report(self, stream, scale):
        """Retrieve the results from the report.

        First retrieve the content of the samples file.
        Second match it against the regex that extract the value of
        `issue_samples`.
        Then convert it to a python list of dictionaries thanks to `ast`.

        Example of retrieved data after conversion (i.e. `raw_report`):
        [{ 'severity': 3, 'type': 40402, 'samples': [
            { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/0' },
            { 'url': 'http://demo.testfire.net/bank/login.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/1' },
            { 'url': 'http://demo.testfire.net/subscribe.aspx', 'extra': 'SQL syntax string', 'sid': '21010', 'dir': '_i2/2' } ]
        },]

        """
        REPORT_VAR_NAME = 'issue_samples'
        res = []
        re_result = self.re_report.findall(stream)
        report = dict({el[0]: el[1] for el in re_result})
        if not REPORT_VAR_NAME in report:
            raise ReportNotFoundError(
                'PTP did NOT find issue_samples variable. Is this the '
                'right file?')
        # We now have a raw version of the Skipfish report as a list of
        # dict.
        for vuln in ast.literal_eval(report[REPORT_VAR_NAME]):
            info = Info(
                # Convert the severity of the issue thanks to an unified
                # ranking scale.
                ranking=scale[vuln['severity']],)
            res.append(info)
        return res
