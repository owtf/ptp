"""

    The Info class will be the summarize of a result form the output report
    provided by pentesting tools.

"""


class Info(object):
    """Representation of a result from a report provided by a pentesting tool.

        + ranking: the ranking of the vulnerability.
        + description: the description of the vulnerability.

    """

    def __init__(self, ranking=None, description=None):
        """Self-explanatory."""
        self.ranking = ranking
        self.description = description

    def __str__(self):
        """String representation of the Info class.

        Can be used to be encoded into a json string and saved into a database.

        """
        return str({'ranking': self.ranking, 'description': self.description})
