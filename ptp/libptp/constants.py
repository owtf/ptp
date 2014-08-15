"""

:synopsis: Constants used across the :mod:`ptp` library.

.. moduleauthor:: Tao Sauvage

"""


#: :class:`int`: Value of an unknown/unranked vulnerability.
UNKNOWN = 0
#: :class:`int`: Value of an informational risk vulnerability.
INFO = 1
#: :class:`int`: Value of a low risk vulnerability.
LOW = 2
#: :class:`int`: Value of a medium risk vulnerability.
MEDIUM = 3
#: :class:`int`: Value of a high risk vulnerability.
HIGH = 4

#: :class:`dict`: :mod:`ptp`'s scale of the ranking values.
RANKING_SCALE = {
    HIGH: HIGH, MEDIUM: MEDIUM, LOW: LOW, INFO: INFO, UNKNOWN: UNKNOWN}
