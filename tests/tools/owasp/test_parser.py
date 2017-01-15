# -*- coding: UTF-8 -*-
import mock
import unittest

from hamcrest import assert_that, has_entry, has_item, has_items, is_not

from ptp.libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH
from ptp.tools.owasp.cm008.parser import OWASPCM008Parser


def handle_file(string, *args, **kwargs):
    if kwargs.get('skip_empty'):
        return [line.rstrip('\n\r') for line in string.splitlines() if line.rstrip('\n\r')]
    return [line.rstrip('\n\r') for line in string.splitlines()]


class TestOWASPCM008Parser(unittest.TestCase):

    ###
    # OWASPCM008Parser.is_mine
    ###
    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_owasp_cm008_is_mine(self, mock_handle):
        from .owasp_cm008_reports import report_low
        self.assertTrue(OWASPCM008Parser.is_mine(report_low))
        from .owasp_cm008_reports import report_medium
        self.assertTrue(OWASPCM008Parser.is_mine(report_medium))
        from .owasp_cm008_reports import report_high
        self.assertTrue(OWASPCM008Parser.is_mine(report_high))

    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_owasp_cm008_is_not_mine(self, mock_handle):
        OWASPCM008Parser.__format__ = ''
        self.assertFalse(OWASPCM008Parser.is_mine('foo.bar'))

    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=OSError)
    def test_parser_owasp_cm008_is_mine_oserror(self, mock_handle):
        OWASPCM008Parser.__format__ = ''
        with self.assertRaises(OSError):
            OWASPCM008Parser.is_mine('foo.bar')

    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=IOError)
    def test_parser_owasp_cm008_is_mine_ioerror(self, mock_handle):
        OWASPCM008Parser.__format__ = ''
        with self.assertRaises(IOError):
            OWASPCM008Parser.is_mine('foo.bar')

    ###
    # OWASPCM008Parser.parse_metadata
    ###
    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_owasp_cm008_parse_metadata(self, mock_handle):
        from .owasp_cm008_reports import report_low
        my_cm008 = OWASPCM008Parser(report_low)
        assert_that(my_cm008.parse_metadata(), has_entry('date', 'Tue, 12 Aug 2014 20:26:16 GMT'))
        from .owasp_cm008_reports import report_medium
        my_cm008 = OWASPCM008Parser(report_medium)
        assert_that(my_cm008.parse_metadata(), has_entry('date', 'Tue, 12 Aug 2014 20:26:16 GMT'))
        from .owasp_cm008_reports import report_high
        my_cm008 = OWASPCM008Parser(report_high)
        assert_that(my_cm008.parse_metadata(), has_entry('date', 'Tue, 12 Aug 2014 20:26:16 GMT'))

    ###
    # OWASPCM008Parser.parse_report
    ###
    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_owasp_cm008_parse_report(self, mock_handle):
        from .owasp_cm008_reports import report_low
        my_cm008 = OWASPCM008Parser(report_low)
        report = my_cm008.parse_report()
        assert_that(report, has_items(*[{'ranking': UNKNOWN}] * 2))
        assert_that(report, has_items(*[{'ranking': LOW}] * 2))
        assert_that(report, is_not(has_item([{'ranking': INFO}])))
        assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .owasp_cm008_reports import report_medium
        my_cm008 = OWASPCM008Parser(report_medium)
        report = my_cm008.parse_report()
        assert_that(report, has_items(*[{'ranking': UNKNOWN}] * 1))
        assert_that(report, has_items(*[{'ranking': MEDIUM}] * 1))
        assert_that(report, is_not(has_item([{'ranking': INFO}])))
        assert_that(report, is_not(has_item([{'ranking': LOW}])))
        assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .owasp_cm008_reports import report_high
        my_cm008 = OWASPCM008Parser(report_high)
        report = my_cm008.parse_report()
        assert_that(report, has_items(*[{'ranking': UNKNOWN}] * 2))
        assert_that(report, has_items(*[{'ranking': LOW}] * 2))
        assert_that(report, has_items(*[{'ranking': HIGH}] * 1))
        assert_that(report, is_not(has_item([{'ranking': INFO}])))
        assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))

    @mock.patch('ptp.libptp.parser.LineParser.handle_file', side_effect=handle_file)
    def test_parser_owasp_cm008_parse_report_no_allow_methods(self, mock_handle):
        from .owasp_cm008_reports import report_no_allow
        my_cm008 = OWASPCM008Parser(report_no_allow)
        self.assertTrue(my_cm008.parse_report() == [])
