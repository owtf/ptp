"""

    OWASP-CM-008 does not provide ranking for the HTTP allowed methods  it has
    found.
    This file tries to define a ranking for each possible method.

"""


from libptp.constants import HIGH, MEDIUM, LOW, INFO


SIGNATURES = {
    'PUT': HIGH,
    'DELETE': HIGH,

    'CONNECT': MEDIUM,

    'TRACE': LOW,
    'HEAD': LOW,
}
