from __future__ import print_function

import os
import traceback

from ptp import PTP
from libptp.tools.metasploit.report import MetasploitReport
from libptp.constants import INFO, LOW, MEDIUM


__testname__ = 'metasploit'


REPORTS = {
    # Scanner
    'auxiliary/scanner/ftp/anonymous': {
        'report_low.metasploit': LOW,
        'report_medium.metasploit': MEDIUM,
    },
    'auxiliary/scanner/ftp/ftp_version': {
        'report_info.metasploit': INFO,
        'report_info2.metasploit': INFO,
    },
    'auxiliary/scanner/ftp/ftp_login': {
        'report_low.metasploit': LOW,
        'report_medium.metasploit': MEDIUM,
    },
    'auxiliary/scanner/smtp/smtp_enum': {
        'report_low.metasploit': LOW,
        'report_low2.metasploit': LOW,
    },
    'auxiliary/scanner/vnc/vnc_login': {
        'report_medium.metasploit': MEDIUM,
        'report_medium2.metasploit': MEDIUM,
    },
    'auxiliary/scanner/vnc/vnc_none_auth': {
        'report_medium.metasploit': MEDIUM,
    },
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
            res = 'ok'
            try:
                ptp.parse(
                    pathname=os.path.join(os.getcwd(), 'tests/metasploit/', plugin),
                    filename=output,
                    plugin=plugin)
            except Exception:
                print(traceback.format_exc())
                res = 'ko'
            print(res)

            print('\t\ttest get_highest_ranking():', end=' ')
            res = 'ok'
            try:
                assert ptp.get_highest_ranking() == outputs[output]
            except Exception:
                print(traceback.format_exc())
                res = 'ko'
            print(res)
