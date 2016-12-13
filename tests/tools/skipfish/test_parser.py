# -*- coding: UTF-8 -*-
import mock
import unittest

from hamcrest import assert_that, has_entries, has_item, has_items, is_not, equal_to

from ptp.libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH
from ptp.tools.skipfish.parser import SkipfishJSParser


class TestSkipfishJSParser(unittest.TestCase):

    ###
    # SkipfishJSParser.parse_metadata
    ###
    @mock.patch('ptp.tools.skipfish.parser.SkipfishJSParser.handle_file', return_value=('', ''))
    @mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[])
    def test_parser_skipfish_parse_metadata(self, mock_find, mock_handle):
        expected_metadata = {'scan_seed': '0x5b37a9a3', 'scan_date': 'Tue May 27 11:31:14 2014', 'scan_ms': '44836', 'sf_version': '2.10b'}
        from .skipfish_reports_2_10_b import report_medium_summary
        my_skipfish = SkipfishJSParser(None)
        my_skipfish.metadata_stream = report_medium_summary
        report = my_skipfish.parse_metadata()
        assert_that(report, has_entries(expected_metadata))
        expected_metadata = {'scan_seed': '0x4491d352', 'sf_version': '2.10b', 'scan_date': 'Mon May 19 20:32:47 2014', 'scan_ms': '2494666'}
        from .skipfish_reports_2_10_b import report_high_summary
        my_skipfish = SkipfishJSParser(None)
        my_skipfish.metadata_stream = report_high_summary
        report = my_skipfish.parse_metadata()
        assert_that(report, has_entries(expected_metadata))

    ###
    # SkipfishJSParser.parse_report
    ###
    @mock.patch('ptp.tools.skipfish.parser.SkipfishJSParser.handle_file', return_value=('', ''))
    @mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[])
    def test_parser_skipfish_parse_report(self, mock_find, mock_handle):
        from .skipfish_reports_2_10_b import report_medium_samples
        my_skipfish = SkipfishJSParser(None)
        my_skipfish.report_stream = report_medium_samples
        report = my_skipfish.parse_report()
        assert_that(report, has_items(*[{'ranking': INFO}] * 3))
        assert_that(report, has_items(*[{'ranking': MEDIUM}] * 2))
        assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
        assert_that(report, is_not(has_item([{'ranking': LOW}])))
        assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .skipfish_reports_2_10_b import report_high_samples
        my_skipfish = SkipfishJSParser(None)
        my_skipfish.__http_parse__ = True
        my_skipfish.report_stream = report_high_samples
        report = my_skipfish.parse_report()
        assert_that(report, has_items(*[{'ranking': INFO}] * 18))
        assert_that(report, has_items(*[{'ranking': LOW}] * 2))
        assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
        assert_that(report, has_items(*[{'ranking': HIGH}] * 1))
        assert_that(389, equal_to(len(report[-1]['transactions'])))
