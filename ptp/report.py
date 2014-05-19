"""

    The Report class will be the summarize of the complete report provided by
    pentesting tools.

"""


from ptp.constants import INFO, RANKING_SCALE
from ptp.info import Info


class AbstractReport(object):
    """Abstract representation of a report provided by a pentesting tool.

        + vulns: List of Info instances

    This class will be extended for each pentesting tool. That way, each tool
    will add its own parser.

    """

    RANKING_SCALE = RANKING_SCALE

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
