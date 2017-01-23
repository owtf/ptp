# -*- coding: UTF-8 -*-
import mock
import unittest

from hamcrest import assert_that, has_items, is_not, has_item

from ptp.libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH
from ptp.tools.robots.parser import RobotsParser


def handle_file(string, *args, **kwargs):
    if kwargs.get('skip_empty'):
        return [line.rstrip('\n\r') for line in string.splitlines() if line.rstrip('\n\r')]
    return [line.rstrip('\n\r') for line in string.splitlines()]


class TestRobotsParser(unittest.TestCase):

    ###
    # RobotsParser.is_mine
    ###
    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_robots_is_mine(self, mock_handle):
        from .robots_reports import report_info
        RobotsParser.__format__ = ''
        self.assertTrue(RobotsParser.is_mine(report_info))

    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_robots_is_not_mine(self, mock_handle):
        RobotsParser.__format__ = ''
        self.assertFalse(RobotsParser.is_mine('foo.bar'))

    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=IOError)
    def test_parser_robots_is_mine_ioerror(self, mock_handle):
        with self.assertRaises(IOError):
            RobotsParser.is_mine('foo.bar')

    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=OSError)
    def test_parser_robots_is_mine_oserror(self, mock_handle):
        with self.assertRaises(OSError):
            RobotsParser.is_mine('foo.bar')

    ###
    # RobotsParser.parse_metadata
    ###
    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_robots_parse_metadata(self, mock_handle):
        from .robots_reports import report_info
        RobotsParser.__format__ = ''
        my_robots = RobotsParser(report_info)
        self.assertTrue(my_robots.parse_metadata() == {})

    ###
    # RobotsParser.parse_report
    ###
    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_robots_parse_report(self, mock_handle):
        from .robots_reports import report_info
        RobotsParser.__format__ = ''
        my_robots = RobotsParser(report_info)
        report = my_robots.parse_report()
        assert_that(report, has_items(*[{'ranking': UNKNOWN}] * 5))
        assert_that(report, has_items(*[{'ranking': INFO}] * 1))
        from .robots_reports import report_unknown
        RobotsParser.__format__ = ''
        my_robots = RobotsParser(report_unknown)
        report = my_robots.parse_report()
        assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
        assert_that(report, is_not(has_item([{'ranking': INFO}])))
        assert_that(report, is_not(has_item([{'ranking': LOW}])))
        assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        assert_that(report, is_not(has_item([{'ranking': HIGH}])))
