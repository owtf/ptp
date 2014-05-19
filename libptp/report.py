"""

    The Report class will be the summarize of the complete report provided by
    pentesting tools.

"""


from libptp import constants


class AbstractReport(object):
    """Abstract representation of a report provided by a pentesting tool.

        + vulns: List of Info instances

    This class will be extended for each pentesting tool. That way, each tool
    will add its own parser.

    """

    RANKING_SCALE = constants.RANKING_SCALE

    def __init__(self, vulns=None):
        """Self-explanatory."""
        self.ranking_scale = self.RANKING_SCALE
        self.vulns = vulns

    def _lowest_ranking(self):
        """From the ranking scale, retrieve the lowest ranking id possible."""
        return min([value for value in self.ranking_scale.values()])

    def _highest_ranking(self):
        """From the ranking scale, retrieve the lowest ranking id possible."""
        return max([value for value in self.ranking_scale.values()])

    def get_highest_ranking(self):
        """Return the highest ranking of the report."""
        highest_possible_ranking = self._highest_ranking()
        # Default highest ranking set to the lowest possible value.
        highest_ranking = self._lowest_ranking()
        for vuln in self.vulns:
            if self.ranking_scale[vuln.ranking] < self.ranking_scale[highest_ranking]:
                highest_ranking = vuln.ranking
            # If the current highest_ranking is already the highest possible
            # one, we can stop the loop.
            if self.ranking_scale[highest_ranking] == highest_possible_ranking:
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
