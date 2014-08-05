from __future__ import print_function

import os
import traceback

from ptp import PTP
from libptp.constants import INFO, HIGH


__testname__ = 'dirbuster'


REPORTS = {
        'report_info.dirbuster': INFO,
        'report_high.dirbuster': HIGH,
}


def run():
    try:
        reports = REPORTS.iteritems()
    except AttributeError:  # Python3
        reports = REPORTS.items()

    for report, ranking in reports:
        ptp = PTP('dirbuster')
        print('\ttest parse():', end=' ')
        res = 'ok'
        try:
            ptp.parse(
                pathname=os.path.join(os.getcwd(), 'tests/dirbuster/1.0'),
                filename=report)
        except Exception:
            print(traceback.format_exc())
            res = 'ko'
        print(res)
        ptp = PTP()
        print('\ttest is_mine():', end=' ')
        res = 'ok'
        try:
            ptp.parse(
                pathname=os.path.join(os.getcwd(), 'tests/dirbuster/1.0'),
                filename=report)
            assert ptp.report.__tool__ == 'dirbuster'
        except Exception:
            print(traceback.format_exc())
            res = 'ko'
        print(res)
        print('\ttest get_highest_ranking():', end=' ')
        res = 'ok'
        try:
            assert ptp.get_highest_ranking() == ranking
        except Exception:
            print(traceback.format_exc())
            res = 'ko'
        print(res)
