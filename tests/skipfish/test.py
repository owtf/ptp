from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import HIGH, MEDIUM


__testname__ = 'skipfish'


def run():
    ptp = PTP('skipfish')
    print('\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(
                os.getcwd(),
                'tests/skipfish/2.10b/demo.testfire.net')
            )
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(
                os.getcwd(),
                'tests/skipfish/2.10b/demo.testfire.net')
            )
        assert ptp.parser.__tool__ == 'skipfish'
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'OK'
    try:
        assert ptp.get_highest_ranking() == HIGH
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP('skipfish')
    print('\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(
                os.getcwd(),
                'tests/skipfish/2.10b/local.xss')
            )
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(
                os.getcwd(),
                'tests/skipfish/2.10b/local.xss')
            )
        assert ptp.parser.__tool__ == 'skipfish'
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'OK'
    try:
        assert ptp.get_highest_ranking() == MEDIUM
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
