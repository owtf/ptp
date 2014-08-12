"""

    Robots.txt might contains interesting Disallow entries.
    This file tries to define a ranking for them.

"""


from libptp.constants import HIGH, MEDIUM, LOW, INFO


# TODO: Complete the signatures database.
SIGNATURES = {
    # Admin interfaces
    '/phpmyadmin': INFO,
    '/admin': INFO,
    '/backend': INFO,
    '/private': INFO,
    '/secret': INFO,
    '/login': INFO,
    '/logon': INFO
}
