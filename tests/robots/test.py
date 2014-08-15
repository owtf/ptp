from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import INFO


__testname__ = 'robots'


def run():
    ptp = PTP('robots')
    print('\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/robots/reports'))
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/robots/reports'))
        assert ptp.parser.__tool__ == 'robots'
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'OK'
    try:
        assert ptp.get_highest_ranking() == INFO
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
