from __future__ import print_function

import os
import traceback

from ptp import PTP


def run():
    ptp = PTP('arachni')
    print('\ttest parse():', end=' ')
    res = 'ok'
    try:
        ptp.parse(pathname=os.path.join(os.getcwd(), 'tests/arachni/0.4.6'))
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'ok'
    try:
        ptp.parse(pathname=os.path.join(os.getcwd(), 'tests/arachni/0.4.6'))
        assert ptp.report.__tool__ == 'arachni'
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'ok'
    try:
        assert ptp.get_highest_ranking() == 0
    except Exception:
        print(traceback.format_exc())
        res = 'ko'
    print(res)
