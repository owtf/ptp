"""

    Metasploit does not provide ranking for the vulnerabilities it has found.
    This file tries to define a ranking for every Metasploit's modules
    discoveries it might find.

"""


from libptp.constants import HIGH, MEDIUM, LOW, INFO


# TODO: Complete the signatures database.
SIGNATURES = {
    # Metasploit's scanner modules.
    'auxiliary/scanner/ftp/anonymous': {
        'Anonymous READ/WRITE ': MEDIUM,
        'has READ/WRITE access': MEDIUM,
        'Anonymous READ ': LOW,
        'has READ access': LOW},

    'auxiliary/scanner/ftp/ftp_version': {
        },

    'auxiliary/scanner/ftp/ftp_login': {
        'Successful authentication': MEDIUM,
        },

    'auxiliary/scanner/smtp/smtp_enum': {
        },

    'auxiliary/scanner/smtp/smtp_version': {
        },

    'auxiliary/fuzzers/smtp/smtp_fuzzer': {
        },

    'auxiliary/scanner/vnc/vnc_login': {
        },

    'auxiliary/scanner/vnc/vnc_none_auth': {
        },

    'auxiliary/scanner/x11/open_x11': {
        },

    'auxiliary/scanner/emc/alphastor_devicemanager': {
        },

    'auxiliary/scanner/emc/alphastor_librarymanager': {
        },

    'auxiliary/scanner/mssql/mssql_ping': {
        },

    'auxiliary/scanner/mssql/mssql_login': {
        },

    'auxiliary/scanner/mssql/mssql_hashdump': {
        },

    'auxiliary/scanner/mssql/mssql_schemadump': {
        },

    'auxiliary/scanner/dcerpc/management': {
        },

    'auxiliary/scanner/dcerpc/endpoint_mapper': {
        },

    'auxiliary/scanner/dcerpc/hidden': {
        },

    'auxiliary/scanner/smb/smb_version': {
        },

    'auxiliary/scanner/smb/pipe_auditor': {
        },

    'auxiliary/scanner/smb/smb_enumusers': {
        },

    'auxiliary/scanner/smb/smb_login': {
        },

    'auxiliary/scanner/snmp/snmp_enumusers': {
        },

    'auxiliary/scanner/snmp/snmp_enumshares': {
        },

    'auxiliary/scanner/snmp/snmp_enum': {
        },

    'auxiliary/scanner/snmp/aix_version': {
        },

    'auxiliary/scanner/snmp/snmp_login': {
        },

    # Metasploit's Exploit modules.
}
