from __future__ import print_function

import os
import traceback

from ptp import PTP
from libptp.tools.owasp.cm008.report import OWASPCM008Report
from libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH


__testname__ = 'owasp'


REPORTS = {
    # Scanner
    'owasp-cm-008': {
        'report_low.txt': LOW,
    }
}


def run():
    try:
        reports = REPORTS.iteritems()
    except AttributeError:  # Python3
        reports = REPORTS.items()

    for test, outputs in reports:
        print('\t> %s' % test)
        for output in outputs:
            ptp = PTP(test)
            print('\t\ttest parse():', end=' ')
            res = 'ok'
            try:
                ptp.parse(
                    pathname=os.path.join(
                        os.getcwd(),
                        'tests/owasp/',
                        test),
                    filename=output)
            except Exception:
                print(traceback.format_exc())
                res = 'ko'
            print(res)

            ptp = PTP()
            print('\t\ttest is_mine():', end=' ')
            res = 'ok'
            try:
                ptp.parse(
                    pathname=os.path.join(
                        os.getcwd(),
                        'tests/owasp/',
                        test),
                    )
                assert ptp.report.__tool__ == 'owasp-cm-008'
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
