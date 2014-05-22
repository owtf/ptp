"""

    Wapiti does not provide ranking for the vulnerabilities it has found.
    This file tries to define a ranking for every vulnerability Wapiti might
    found.

"""


from libptp.constants import HIGH, MEDIUM, LOW, INFO


# TODO: Complete the signatures database.
SIGNATURES = {
    'SQL Injection': HIGH,
    'Blind SQL Injection': HIGH,
    'Command execution': HIGH,
}
