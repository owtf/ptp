from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH


__testname__ = 'metasploit'


REPORTS = {
    # Scanner
    'auxiliary/scanner/ftp/anonymous': {
        'report_low.txt': LOW,
        'report_high.txt': HIGH,
    },
    'auxiliary/scanner/ftp/ftp_version': {
        'report_info.txt': INFO,
        'report_info2.txt': INFO,
    },
    'auxiliary/scanner/ftp/ftp_login': {
        'report_low.txt': LOW,
        'report_high.txt': HIGH,
    },
    'auxiliary/scanner/smtp/smtp_enum': {
        'report_low.txt': LOW,
        'report_low2.txt': LOW,
    },
    'auxiliary/scanner/vnc/vnc_login': {
        'report_high.txt': HIGH,
        'report_high2.txt': HIGH,
    },
    'auxiliary/scanner/vnc/vnc_none_auth': {
        'report_high.txt': HIGH,
    },
    'auxiliary/scanner/x11/open_x11': {
        'report_high.txt': HIGH,
        'report_high2.txt': HIGH,
    },
    # TODO: Add report examples for EMC AlphaStor.
    'auxiliary/scanner/mssql/mssql_ping': {
        'report_info.txt': INFO,
        'report_info2.txt': INFO,
        'report_info3.txt': INFO,
    },
    'auxiliary/scanner/mssql/mssql_login': {
        'report_high.txt': HIGH,
        'report_high2.txt': HIGH,
    },
    'auxiliary/scanner/mssql/mssql_hashdump': {
        'report_high.txt': HIGH,
    },
    # TODO: Add report examples for MSSQL Schema dump.
    # TODO: Add report examples for DCERPC endpoint mapper.
    # TODO: Add report examples for DCERPC hidden.
    'auxiliary/scanner/smb/smb_version': {
        'report_info.txt': INFO,
        'report_info2.txt': INFO,
        'report_info3.txt': INFO,
    },
    'auxiliary/scanner/smb/pipe_auditor': {
        'report_info.txt': INFO,
        'report_info2.txt': INFO,
    },
    'auxiliary/scanner/smb/smb_enumusers': {
        'report_info.txt': INFO,
        'report_info2.txt': INFO,
        'report_info3.txt': INFO,
    },
    'auxiliary/scanner/smb/smb_login': {
        'report_high.txt': HIGH,
        'report_high2.txt': HIGH,
        'report_unknown.txt': UNKNOWN,
    },
    'auxiliary/scanner/snmp/snmp_enumusers': {
        'report_low.txt': LOW,
    },
    # FIXME: Fix the snmp_enumshares signature.
    #'auxiliary/scanner/snmp/snmp_enumshares': {
    #    'report_low.txt': LOW,
    #},
    # TODO: Add report examples for SNMP enums.
    # TODO: Add report examples for SNMP AIX version.
    'auxiliary/scanner/snmp/snmp_login': {
        'report_low.txt': LOW,
        'report_high.txt': HIGH,
        'report_high2.txt': HIGH,
    }
}


def run():
    try:
        reports = REPORTS.iteritems()
    except AttributeError:  # Python3
        reports = REPORTS.items()

    for plugin, outputs in reports:
        print('\t> %s' % plugin)
        for output in outputs:
            ptp = PTP('metasploit')
            print('\t\ttest parse():', end=' ')
            res = 'OK'
            try:
                ptp.parse(
                    pathname=os.path.join(
                        os.getcwd(),
                        'tests/metasploit/',
                        plugin),
                    filename=output,
                    plugin=plugin)
            except Exception:
                print(traceback.format_exc())
                res = 'FAIL'
            print(res)

            print('\t\ttest get_highest_ranking():', end=' ')
            res = 'OK'
            try:
                assert ptp.get_highest_ranking() == outputs[output]
            except Exception:
                print(traceback.format_exc())
                res = 'FAIL'
            print(res)
