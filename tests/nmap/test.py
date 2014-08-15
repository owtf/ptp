from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import INFO, HIGH


__testname__ = 'nmap'


def run():
    ptp = PTP('nmap')
    print('\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/nmap/6.46'))
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/nmap/6.46'))
        assert ptp.parser.__tool__ == 'nmap'
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
