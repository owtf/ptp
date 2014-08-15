from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import LOW, HIGH


__testname__ = 'dirbuster'


REPORTS = {
        'DirBuster-Report-low.txt': LOW,
        'DirBuster-Report-high.txt': HIGH,
}


def run():
    try:
        reports = REPORTS.iteritems()
    except AttributeError:  # Python3
        reports = REPORTS.items()

    for report, ranking in reports:
        ptp = PTP('dirbuster')
        print('\ttest parse():', end=' ')
        res = 'OK'
        try:
            ptp.parse(
                pathname=os.path.join(os.getcwd(), 'tests/dirbuster/1.0'),
                filename=report)
        except Exception:
            print(traceback.format_exc())
            res = 'FAIL'
        print(res)
        ptp = PTP()
        print('\ttest is_mine():', end=' ')
        res = 'OK'
        try:
            ptp.parse(
                pathname=os.path.join(os.getcwd(), 'tests/dirbuster/1.0'),
                filename=report)
            assert ptp.parser.__tool__ == 'dirbuster'
        except Exception:
            print(traceback.format_exc())
            res = 'FAIL'
        print(res)
        print('\ttest get_highest_ranking():', end=' ')
        res = 'OK'
        try:
            assert ptp.get_highest_ranking() == ranking
        except Exception:
            print(traceback.format_exc())
            res = 'FAIL'
        print(res)
