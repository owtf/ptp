"""

    Metasploit does not provide ranking for the vulnerabilities it has found.
    This file tries to define a ranking for every Metasploit's modules
    discoveries it might find.

"""


from libptp.constants import HIGH, MEDIUM, LOW, INFO, HIGH


# TODO: Complete the signatures database.
SIGNATURES = {
    # Metasploit's scanner modules.
    'auxiliary/scanner/ftp/anonymous': {
        'Anonymous READ/WRITE ': HIGH,
        'Anonymous READ ': LOW,
        },

    'auxiliary/scanner/ftp/ftp_version': {
        'FTP Banner': INFO,
        },

    'auxiliary/scanner/ftp/ftp_login': {
        'has READ/WRITE access': HIGH,
        'has READ access': LOW,
        },

    'auxiliary/scanner/smtp/smtp_enum': {
        'Found user': LOW,
        'Users found': LOW,
        },

    'auxiliary/scanner/smtp/smtp_version': {
        'SMTP': INFO,
        },

    'auxiliary/scanner/vnc/vnc_login': {
        'VNC server password': HIGH,
        },

    'auxiliary/scanner/vnc/vnc_none_auth': {
        'free access': HIGH,
        },

    'auxiliary/scanner/x11/open_x11': {
        'Open X Server': HIGH,
        },

    'auxiliary/scanner/emc/alphastor_devicemanager': {
        'is running the EMC AlphaStor Device Manager': INFO,
        },

    'auxiliary/scanner/emc/alphastor_librarymanager': {
        'is running the EMC AlphaStor Library Manager': INFO,
        },

    'auxiliary/scanner/mssql/mssql_ping': {
        'SQL Server information for': INFO,
        },

    'auxiliary/scanner/mssql/mssql_login': {
        'MSSQL - successful login': HIGH,
        'successful logged in as': HIGH,
        },

    # TODO: Enhance the matching string.
    'auxiliary/scanner/mssql/mssql_hashdump': {
        'Saving': HIGH,
        },

    'auxiliary/scanner/mssql/mssql_schemadump': {
        'Microsoft SQL Server Schema': HIGH,
        },

    # TODO: Complete the matching strings.
    'auxiliary/scanner/dcerpc/management': {
        },

    'auxiliary/scanner/dcerpc/endpoint_mapper': {
        'Endpoint Mapper': INFO,
        },

    'auxiliary/scanner/dcerpc/hidden': {
        'HIDDEN: UUID': INFO,
        },

    'auxiliary/scanner/smb/smb_version': {
        'is running': INFO,
        },

    'auxiliary/scanner/smb/pipe_auditor': {
        '- Pipes:': INFO,
        },

    # TODO: Enhance the matching string (using regexp IMO).
    'auxiliary/scanner/smb/smb_enumusers': {
        ', ': INFO,
        },

    'auxiliary/scanner/smb/smb_login': {
        'SUCCESSFUL LOGIN': HIGH,
        },

    'auxiliary/scanner/snmp/snmp_enumusers': {
        'Found Users': LOW,
        },

    # TODO: Enhance the matching string (using regexp IMO).
    'auxiliary/scanner/snmp/snmp_enumshares': {
        ' - ': LOW,
        },

    'auxiliary/scanner/snmp/snmp_enum': {
        ', Connected.': INFO,
        },

    'auxiliary/scanner/snmp/aix_version': {
        'IBM AIX Version': INFO,
        },

    'auxiliary/scanner/snmp/snmp_login': {
        'community string': LOW,
        'provides READ-ONLY access': LOW,
        'provides READ-WRITE access': HIGH,
        },

    # Metasploit's fuzzer modules.
    # TODO: Complete the matching strings.
    'auxiliary/fuzzers/smtp/smtp_fuzzer': {
        },

    # Metasploit's Exploit modules.
}
