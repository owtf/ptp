# -*- coding: UTF-8 -*-
import mock
import unittest

from hamcrest import assert_that, has_items

from ptp.libptp.constants import LOW, HIGH
from ptp.tools.dirbuster.parser import DirbusterParser


def handle_file(string, *args, **kwargs):
    if kwargs.get('skip_empty'):
        return [line.rstrip('\n\r') for line in string.splitlines() if line.rstrip('\n\r')]
    return [line.rstrip('\n\r') for line in string.splitlines()]


class TestDirbusterParser(unittest.TestCase):

    ###
    # DirbusterParser.is_mine
    ###
    def test_parser_dirbuster_is_mine(self):
        # Dirbuster 1.0-RC1
        from .dirbuster_reports import report_low
        with mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file):
            DirbusterParser.__format__ = ''
            self.assertTrue(DirbusterParser.is_mine(report_low))
        from .dirbuster_reports import report_high
        with mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file):
            DirbusterParser.__format__ = ''
            self.assertTrue(DirbusterParser.is_mine(report_high))

    def test_parser_dirbuster_is_not_mine(self):
        with mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file):
            DirbusterParser.__format__ = ''
            self.assertFalse(DirbusterParser.is_mine('foo.bar'))

    ###
    # DirbusterParser.parse_metadata
    ###
    def test_parser_dirbuster_parse_metadata(self):
        # Dirbuster 1.0-RC1
        from .dirbuster_reports import report_low
        with mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file):
            DirbusterParser.__format__ = ''
            my_dirbuster = DirbusterParser(report_low)
            metadata = my_dirbuster.parse_metadata()
            self.assertTrue(metadata.get('version', '') == '1.0-RC1')
        from .dirbuster_reports import report_high
        with mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file):
            DirbusterParser.__format__ = ''
            my_dirbuster = DirbusterParser(report_high)
            metadata = my_dirbuster.parse_metadata()
            self.assertTrue(metadata.get('version', '') == '1.0-RC1')

    ###
    # DirbusterParser.parse_report
    ###
    def test_parser_dirbuster_parse_report(self):
        # Dirbuster 1.0-RC1
        from .dirbuster_reports import report_low
        with mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file):
            DirbusterParser.__format__ = ''
            my_dirbuster = DirbusterParser(report_low)
            assert_that(my_dirbuster.parse_report(), has_items(*[{'ranking': LOW}] * 1))
        from .dirbuster_reports import report_high
        with mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file):
            DirbusterParser.__format__ = ''
            my_dirbuster = DirbusterParser(report_high)
            assert_that(my_dirbuster.parse_report(), has_items(*[{'ranking': HIGH}] * 1))
