from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import HIGH, MEDIUM


__testname__ = 'wapiti'


def run():
    ptp = PTP('wapiti')
    print('\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/wapiti/2.3.0'))
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/wapiti/2.3.0'))
        assert ptp.parser.__tool__ == 'wapiti'
        assert '2.3.0' in ptp.parser.__version__
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

    print('\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(pathname=os.path.join(os.getcwd(), 'tests/wapiti/2.2.1'))
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/wapiti/2.2.1'))
        assert ptp.parser.__tool__ == 'wapiti'
        assert '2.2.1' in ptp.parser.__version__
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'OK'
    try:
        # Haha, Wapiti 2.2.1 detects SQL injections that 2.3.0 doesn't.
        assert ptp.get_highest_ranking() == HIGH
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
