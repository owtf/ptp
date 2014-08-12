from __future__ import print_function

import os
import traceback

from ptp import PTP
from libptp.constants import INFO


__testname__ = 'robots'


def run():
    ptp = PTP('robots')
    print('\ttest parse():', end=' ')
    res = 'ok'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/robots/reports'))
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'ok'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/robots/reports'))
        assert ptp.report.__tool__ == 'robots'
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'ok'
    try:
        assert ptp.get_highest_ranking() == INFO
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
