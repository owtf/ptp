#!/usr/bin/env python
from __future__ import print_function

import os
import sys
import imp
import fnmatch

# Test directory
DIR_TEST = 'tests'


def find_tests(pathname):
    """Recursively finds the test modules.

    :param str pathname: Path name where the tests are stored.
    :returns: List of paths to each test modules.
    :rtype: :class:`list`

    """
    founds = []
    for base, _, files in os.walk(pathname):
        founds.extend((
            (matched_file, base)
            for matched_file in fnmatch.filter(files, '*.py')
            if matched_file != "__init__.py"))
    return founds


def run_tests(pathnames=None, test_name=None):
    """Loads each test module and run their `run` function.

    :param list pathnames: List of (module_name, path_to_the_module).

    """
    if pathnames is None:
        pathnames = find_tests(os.path.join(os.getcwd(), DIR_TEST))
    for module, path in pathnames:
        current_mod = imp.load_source(
            os.path.splitext(module)[0],
            os.path.join(path, module))
        if test_name and test_name != current_mod.__testname__:
            continue
        print("Testing:", current_mod.__testname__)
        current_mod.run()


if __name__ == '__main__':
    test_name = None
    if len(sys.argv) == 2:
        test_name = sys.argv[1]
    run_tests(find_tests(os.path.join(os.getcwd(), DIR_TEST)), test_name)
