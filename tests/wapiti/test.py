from __future__ import print_function

import os
import re
import traceback

from ptp import PTP
from ptp.libptp.constants import HIGH, MEDIUM


__testname__ = 'wapiti'


def run():
    print("\ttesting version 2.3.0")
    ptp = PTP('wapiti')
    print('\t\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/wapiti/2.3.0'))
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\t\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/wapiti/2.3.0'))
        assert ptp.parser.__tool__ == 'wapiti'
        assert re.match(ptp.parser.__version__, '2.3.0', flags=re.IGNORECASE)
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    print('\t\ttest get_highest_ranking():', end=' ')
    res = 'OK'
    try:
        assert ptp.get_highest_ranking() == MEDIUM
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)

    print("\ttesting version 2.2.1")
    print('\t\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(pathname=os.path.join(os.getcwd(), 'tests/wapiti/2.2.1'))
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\t\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/wapiti/2.2.1'))
        assert ptp.parser.__tool__ == 'wapiti'
        assert re.match(ptp.parser.__version__, '2.2.1', flags=re.IGNORECASE)
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    print('\t\ttest get_highest_ranking():', end=' ')
    res = 'OK'
    try:
        # Haha, Wapiti 2.2.1 detects SQL injections that 2.3.0 doesn't.
        assert ptp.get_highest_ranking() == HIGH
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
