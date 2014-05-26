from __future__ import print_function
import os
from ptp import PTP
from libptp.tools.wapiti.wapiti import WapitiReport


def run():
    ptp = PTP('w3af')
    print('\ttest parse():', end=' ')
    res = 'ok'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/w3af/1.6.0.2'))
    except ValueError:
        res = 'ko'
    print(res)
    ptp = PTP()
    print('\ttest is_mine():', end=' ')
    res = 'ok'
    try:
        ptp.parse(
            pathname=os.path.join(os.getcwd(), 'tests/w3af/1.6.0.2'))
        assert ptp.report.__tool__ == 'w3af'
    except:
        res = 'ko'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'ok'
    try:
        assert ptp.get_highest_ranking() == 0
    except AssertionError:
        res = 'ko'
    print(res)
