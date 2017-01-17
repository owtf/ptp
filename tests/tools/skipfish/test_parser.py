# -*- coding: UTF-8 -*-
import mock
import unittest

from hamcrest import assert_that, has_entries, has_item, has_items, is_not, equal_to

from ptp.libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH
from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.tools.skipfish.parser import SkipfishJSParser


class TestSkipfishJSParser(unittest.TestCase):

    def setUp(self):
        self.ori_format = SkipfishJSParser.__format__

    def tearDown(self):
        SkipfishJSParser.__format__ = self.ori_format

    ###
    # SkipfishJSParser.__init__
    ###
    def test_parser_skipfish_init_valid_pathname(self):
        from .skipfish_reports_2_10_b import report_medium_summary, report_medium_samples
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=['foo', 'bar']):
            with mock.patch('ptp.tools.skipfish.parser.SkipfishJSParser.handle_file', return_value=[report_medium_summary, report_medium_samples]):
                my_skipfish = SkipfishJSParser(pathname='foo/bar')
                self.assertTrue(my_skipfish.metadata_stream and my_skipfish.metadata_stream == report_medium_summary)
                self.assertTrue(my_skipfish.report_stream and my_skipfish.report_stream == report_medium_samples)

    ###
    # SkipfishJSParser.handle_file
    ###
    def test_parser_skipfish_handle_file_invalid_extension(self):
        with self.assertRaises(TypeError):
            SkipfishJSParser.handle_file(metadatafile='invalid.asdfdsaasdfsadfsdf', reportfile='valid.js')
        with self.assertRaises(TypeError):
            SkipfishJSParser.handle_file(metadatafile='valid.js', reportfile='invalid.asdfdsaasdfsadfsdf')

    def test_parser_skipfish_handle_file_valid_extension_but_file_not_found(self):
        # TODO: Test for a valid metadatafile but a reportfile that cannot be found.
        with self.assertRaises(IOError):
            SkipfishJSParser.handle_file(metadatafile='filethatdoesnotexistihopeatleastfortesting.js', reportfile='valid.js')

    def test_parser_skipfish_handle_file_valid_extension_and_valid_file(self):
        with mock.patch('ptp.libptp.parser.FileParser.handle_file', side_effect=['metadata', 'report']):
            SkipfishJSParser.__format__ = ''
            metadata, report = SkipfishJSParser.handle_file(metadatafile='foo', reportfile='bar')
            self.assertTrue(metadata == 'metadata')
            self.assertTrue(report == 'report')

    ###
    # SkipfishJSParser.is_mine
    ###
    def test_parser_skipfish_is_mine_no_metadata(self):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[]):
            SkipfishJSParser.__format__ = ''
            self.assertFalse(SkipfishJSParser.is_mine(pathname='foo/bar'))

    def test_parser_skipfish_is_mine_metadata_but_no_report(self):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', side_effect=[['foo'], []]):
            SkipfishJSParser.__format__ = ''
            self.assertFalse(SkipfishJSParser.is_mine(pathname='foo/bar'))

    def test_parser_skipfish_is_mine_metadata_and_report_but_invalid_extension(self):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', side_effect=[['foo'], ['bar']]):
            SkipfishJSParser.__format__ = 'js'
            self.assertFalse(SkipfishJSParser.is_mine(pathname='foo/bar'))

    def test_parser_skipfish_is_mine_metadata_and_report_and_invalid_extension(self):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', side_effect=[['foo.js'], ['bar.js']]):
            with mock.patch('ptp.tools.skipfish.parser.SkipfishJSParser.handle_file', return_value=['metadata', 'report']):
                SkipfishJSParser.__format__ = ''
                self.assertTrue(SkipfishJSParser.is_mine(pathname='foo/bar'))
    ###
    # SkipfishJSParser.parse_metadata
    ###
    def test_parser_skipfish_parse_metadata_unsupported_version(self):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', side_effect=[['foo'], ['bar']]):
            with mock.patch('ptp.tools.skipfish.parser.SkipfishJSParser.handle_file', return_value=["var variable = 'value';", 'report']):
                SkipfishJSParser.__format__ = ''
                my_skipfish = SkipfishJSParser(pathname='foo/bar')
                with self.assertRaises(NotSupportedVersionError):
                    my_skipfish.parse_metadata()

    @mock.patch('ptp.tools.skipfish.parser.SkipfishJSParser.handle_file', return_value=('', ''))
    @mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[])
    def test_parser_skipfish_parse_metadata_valid(self, mock_find, mock_handle):
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
        my_skipfish.report_stream = report_high_samples
        report = my_skipfish.parse_report()
        assert_that(report, has_items(*[{'ranking': INFO}] * 18))
        assert_that(report, has_items(*[{'ranking': LOW}] * 2))
        assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
        assert_that(report, has_items(*[{'ranking': HIGH}] * 1))
        assert_that(389, equal_to(len(report[-1]['transactions'])))
