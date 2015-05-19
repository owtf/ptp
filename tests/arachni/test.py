from __future__ import print_function

import os
import traceback

from ptp import PTP
from ptp.libptp.constants import LOW, HIGH


__testname__ = 'arachni'


TESTPATH = 'tests/arachni'
TESTFILES = {
    '0.4.6': {'demo.testfire.net.xml': HIGH},
    '1.0': {
        'local.site.xml': LOW,
        'local2.site.xml': HIGH},
    '1.0.1': {
        'local.site.xml': LOW,
        'local2.site.xml': HIGH},
    '1.0.2': {
        'local.site.xml': LOW,
        'local2.site.xml': HIGH},
    '1.0.3': {
        'local.site.xml': LOW,
        'local2.site.xml': HIGH},
    '1.0.4': {
        'local.site.xml': LOW,
        'local2.site.xml': HIGH},
    '1.0.5': {
        'local.site.xml': LOW,
        'local2.site.xml': HIGH},
    '1.0.6': {
        'local.site.xml': LOW,
        'local2.site.xml': HIGH},
    '1.1': {
        'local.site.xml': LOW,
        'local2.site.xml': HIGH},
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
            assert ptp.parser.__tool__ == 'arachni'
        except Exception:
            print(traceback.format_exc())
            res = 'FAIL'
        print(res)
        ptp = PTP('arachni')
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
            ptp = PTP('arachni')
            print('\t\ttest is_mine():', end=' ')
            res = 'OK'
            try:
                ptp.parse(
                    pathname=os.path.join(os.getcwd(), '%s/%s' % (TESTPATH, version)),
                    filename=testfile)
                assert ptp.parser.__tool__ == 'arachni'
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
