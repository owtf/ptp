"""

:synopsis: OWASP-CM-008 does not provide ranking for the HTTP allowed methods
    it has found. This file tries to define a ranking for each possible method.

.. moduleauthor:: Tao Sauvage

"""


from ptp.libptp.constants import HIGH, MEDIUM, LOW


# TODO: Complete the methods signatures database.
#: :data: :class:`dict` of the methods with their rank.
SIGNATURES = {
    'PUT': HIGH,
    'DELETE': HIGH,

    'CONNECT': MEDIUM,

    'TRACE': LOW,
    'HEAD': LOW,
}
