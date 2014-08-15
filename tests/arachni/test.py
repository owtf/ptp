from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import HIGH


__testname__ = 'arachni'


def run():
    ptp = PTP('arachni')
    print('\ttest parse():', end=' ')
    res = 'OK'
    try:
        ptp.parse(pathname=os.path.join(os.getcwd(), 'tests/arachni/0.4.6'))
    except Exception:
        print(traceback.format_exc())
        res = 'FAIL'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'OK'
    try:
        ptp.parse(pathname=os.path.join(os.getcwd(), 'tests/arachni/0.4.6'))
        assert ptp.parser.__tool__ == 'arachni'
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
