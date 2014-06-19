from __future__ import print_function

import os
import traceback

from ptp import PTP


def run():
    ptp = PTP('skipfish')
    print('\ttest parse():', end=' ')
    res = 'ok'
    try:
        ptp.parse(
            pathname=os.path.join(
                os.getcwd(),
                'tests/skipfish/2.10b/demo.testfire.net')
            )
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'ok'
    try:
        ptp.parse(
            pathname=os.path.join(
                os.getcwd(),
                'tests/skipfish/2.10b/demo.testfire.net')
            )
        assert ptp.report.__tool__ == 'skipfish'
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'ok'
    try:
        assert ptp.get_highest_ranking() == 0  # Hight
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    ptp = PTP('skipfish')
    print('\ttest parse():', end=' ')
    res = 'ok'
    try:
        ptp.parse(
            pathname=os.path.join(
                os.getcwd(),
                'tests/skipfish/2.10b/local.xss')
            )
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'ok'
    try:
        ptp.parse(
            pathname=os.path.join(
                os.getcwd(),
                'tests/skipfish/2.10b/local.xss')
            )
        assert ptp.report.__tool__ == 'skipfish'
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'ok'
    try:
        assert ptp.get_highest_ranking() == 1  # Medium
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
