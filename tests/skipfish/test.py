from __future__ import print_function
import os
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
    except ValueError:
        res = 'ko'
    print(res)
    print('\ttest get_highest_ranking():', end=' ')
    res = 'ok'
    try:
        assert ptp.get_highest_ranking() == 0
    except AssertionError:
        res = 'ko'
    print(res)
