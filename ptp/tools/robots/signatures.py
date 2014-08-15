"""

:synopsis: Robots.txt might contains interesting Disallow entries. This file
    tries to define a ranking for them.

"""


from ptp.libptp.constants import INFO


# TODO: Complete the signatures database.
#: :data: :class:`dict` of the methods with their rank.
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
