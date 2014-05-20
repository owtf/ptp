"""

    The Report class will be the summarize of the complete report provided by
    pentesting tools.

"""


from libptp.constants import RANKING_SCALE


class AbstractReport(object):
    """Abstract representation of a report provided by a pentesting tool.

        + vulns: List of Info instances

    This class will be extended for each pentesting tool. That way, each tool
    will add its own parser.

    """

    def __init__(self, vulns=None):
        """Self-explanatory."""
        self.vulns = vulns

    def __str__(self):
        return ', '.join([info.__str__() for info in self.vulns])

    def _lowest_ranking(self):
        """From the ranking scale, retrieve the lowest ranking id possible."""
        return min([value for value in RANKING_SCALE.values()])

    def _highest_ranking(self):
        """From the ranking scale, retrieve the lowest ranking id possible."""
        return max([value for value in RANKING_SCALE.values()])

    def get_highest_ranking(self, path_to_report=None):
        """Return the highest ranking of the report."""
        # Be sure that the parsing already happened.
        if self.vulns is None:
            if path_to_report is None:
                raise ValueError('A path to the report SHOULD be specified.')
            self.parser(path_to_report)
        highest_possible_ranking = self._highest_ranking()
        # Default highest ranking set to the lowest possible value.
        highest_ranking = self._lowest_ranking()
        for vuln in self.vulns:
            if RANKING_SCALE[vuln.ranking] < RANKING_SCALE[highest_ranking]:
                highest_ranking = vuln.ranking
            # If the current highest_ranking is already the highest possible
            # one, we can stop the loop.
            if RANKING_SCALE[highest_ranking] == highest_possible_ranking:
                break
        return highest_ranking

    def from_file(self, pathname):
        """Read the content of a report from its file and parse it."""
        with open(pathname, 'r') as f:
            raw_data = f.read()
        self.raw_data = raw_data
        self.parser(self.raw_data)

    def from_stream(self, data):
        """Read the content of a report for its data and parse it."""
        self.raw_data = data
        self.parser(self.raw_data)

    def parser(self, data):
        """Abstract parser that will parse the report of a tool."""
        raise NotImplementedError('The parser MUST be define for each tool.')
