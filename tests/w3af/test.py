from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import MEDIUM, HIGH


__testname__ = 'w3af'


TESTPATH = 'tests/w3af'
TESTFILES = {
    '1.6.0.2': {'demo.testfire.net.xml': HIGH},
    '1.6.0.3': {
        'local.site.xml': MEDIUM,
        'local2.site.xml': HIGH},
    '1.6.0.5': {
        'local.site.xml': MEDIUM,
        'local2.site.xml': HIGH},
    '1.6.45': {
        'local.site.xml': MEDIUM,
        'local2.site.xml': HIGH},
    '1.6.46': {
        'local.site.xml': MEDIUM,
        'local2.site.xml': HIGH},
    '1.6.49': {
        'local.site.xml': MEDIUM,
        'local2.site.xml': HIGH},
    '1.6.50': {
        'local.site.xml': MEDIUM,
        'local2.site.xml': HIGH},
    '1.6.51': {
        'local.site.xml': MEDIUM,
        'local2.site.xml': HIGH}
}


def run():
    try:
        versions = TESTFILES.iterkeys()
    except AttributeError:  # Python3
        versions = TESTFILES.keys()

    for version in versions:
        print("\ttesting version '%s' (auto)" % version)
        ptp = PTP()
        print('\t\ttest is_mine():', end=' ')
        res = 'OK'
        try:
            ptp.parse(pathname=os.path.join(os.getcwd(), '%s/%s' % (TESTPATH, version)))
            assert ptp.parser.__tool__ == 'w3af'
        except Exception:
            print(traceback.format_exc())
            res = 'FAIL'
        print(res)
        ptp = PTP('w3af')
        print('\t\ttest parse():', end=' ')
        res = 'OK'
        try:
            ptp.parse(pathname=os.path.join(os.getcwd(), '%s/%s' % (TESTPATH, version)))
        except Exception:
            print(traceback.format_exc())
            res = 'FAIL'
        print(res)

        print("\ttesting version '%s' (manual)" % version)
        try:
            couples = TESTFILES[version].iteritems()
        except AttributeError:  # Python3
            couples = TESTFILES[version].items()
        for testfile, ranking in couples:
            ptp = PTP('w3af')
            print('\t\ttest is_mine():', end=' ')
            res = 'OK'
            try:
                ptp.parse(
                    pathname=os.path.join(os.getcwd(), '%s/%s' % (TESTPATH, version)),
                    filename=testfile)
                assert ptp.parser.__tool__ == 'w3af'
            except Exception:
                print(traceback.format_exc())
                res = 'FAIL'
            print(res)
            print('\t\ttest parse():', end=' ')
            res = 'OK'
            try:
                ptp.parse(
                    pathname=os.path.join(os.getcwd(), '%s/%s' % (TESTPATH, version)),
                    filename=testfile)
            except Exception:
                print(traceback.format_exc())
                res = 'FAIL'
            print(res)
            print('\t\ttest get_highest_ranking():', end=' ')
            res = 'OK'
            try:
                assert ptp.get_highest_ranking() == ranking
            except Exception:
                print(traceback.format_exc())
                res = 'FAIL'
            print(res)
