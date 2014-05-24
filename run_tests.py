from __future__ import print_function
from tests.arachni.test import run as arachni_run
from tests.skipfish.test import run as skipfish_run
from tests.w3af.test import run as w3af_run
from tests.wapiti.test import run as wapiti_run


if __name__ == '__main__':
    print('# Running Arachni:')
    arachni_run()
    print('# Running Skipfish:')
    skipfish_run()
    print('# Running W3AF:')
    w3af_run()
    print('# Running Wapiti:')
    wapiti_run()
