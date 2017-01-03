# -*- coding: UTF-8 -*-
import unittest

from hamcrest import assert_that, has_item, is_not, equal_to

from ptp.libptp import constants
from ptp.libptp.exceptions import NotSupportedToolError
from ptp import PTP

from .utils import MockParser, MockParserInfo, MockParserHigh


class TestPTP(unittest.TestCase):

    ###
    # PTP.__init__
    ###
    def test_ptp_init_unsupported_tool(self):
        with self.assertRaises(NotSupportedToolError):
            PTP(tool_name='AToolWithANameThatWouldNeverExistAndEvenIfItExistedItWontBeSupported')

    def test_ptp_init_supported_tools(self):
        tool_names = [
            'arachni', 'skipfish', 'w3af', 'wapiti', 'metasploit', 'dirbuster', 'nmap', 'owasp-cm-008', 'robots',
            'burpsuite', 'hoppy']
        for tool_name in tool_names:
            self.assertTrue(PTP(tool_name=tool_name).tool_name == tool_name)

    def test_ptp_init_unspecified_tool(self):
        self.assertTrue(PTP().tool_name == '')

    ###
    # PTP._init_parser
    ###
    def test_ptp_init_parser_no_tool(self):
        my_ptp = PTP()
        my_ptp._init_parser()
        self.assertIsNone(my_ptp.parser)

    ###
    # PTP.parse
    ###
    def test_ptp_parse_no_tool(self):
        my_ptp = PTP()
        with self.assertRaises(NotSupportedToolError):
            my_ptp.parse()

    def test_ptp_parse_mock_parser(self):
        my_ptp = PTP()
        my_ptp.parser = MockParser()
        vulns = my_ptp.parse()
        self.assertEqual(vulns, [])
        self.assertEqual(my_ptp.tool_name, 'mock')
        self.assertEqual(my_ptp.metadata, {})

    ###
    # PTP.get_highest_ranking
    ###
    def test_ptp_get_highest_ranking_no_vuln(self):
        self.assertTrue(PTP().get_highest_ranking() == constants.UNKNOWN)

    def test_ptp_get_highest_ranking_vuln_with_no_ranking(self):
        my_ptp = PTP()
        my_ptp.vulns = [{'foo': 'bar'}]
        self.assertTrue(my_ptp.get_highest_ranking() == constants.UNKNOWN)

    def test_ptp_get_highest_ranking_unknown_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [{'ranking': constants.UNKNOWN}]
        self.assertTrue(my_ptp.get_highest_ranking() == constants.UNKNOWN)

    def test_ptp_get_highest_ranking_info_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [{'ranking': constants.UNKNOWN}, {'ranking': constants.INFO}]
        self.assertTrue(my_ptp.get_highest_ranking() == constants.INFO)

    def test_ptp_get_highest_ranking_low_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [{'ranking': constants.UNKNOWN}, {'ranking': constants.INFO}, {'ranking': constants.LOW}]
        self.assertTrue(my_ptp.get_highest_ranking() == constants.LOW)

    def test_ptp_get_highest_ranking_medium_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [
            {'ranking': constants.UNKNOWN}, {'ranking': constants.INFO}, {'ranking': constants.LOW},
            {'ranking': constants.MEDIUM}]
        self.assertTrue(my_ptp.get_highest_ranking() == constants.MEDIUM)

    def test_ptp_get_highest_ranking_high_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [
            {'ranking': constants.UNKNOWN}, {'ranking': constants.INFO}, {'ranking': constants.LOW},
            {'ranking': constants.MEDIUM}, {'ranking': constants.HIGH}]
        self.assertTrue(my_ptp.get_highest_ranking() == constants.HIGH)

    ###
    # PTP.highest_ranking
    ###
    def test_ptp_highest_ranking_no_vuln(self):
        self.assertTrue(PTP().highest_ranking == constants.UNKNOWN)

    def test_ptp_highest_ranking_vuln_with_no_ranking(self):
        my_ptp = PTP()
        my_ptp.vulns = [{'foo': 'bar'}]
        self.assertTrue(my_ptp.highest_ranking == constants.UNKNOWN)

    def test_ptp_highest_ranking_unknown_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [{'ranking': constants.UNKNOWN}]
        self.assertTrue(my_ptp.highest_ranking == constants.UNKNOWN)

    def test_ptp_highest_ranking_info_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [{'ranking': constants.UNKNOWN}, {'ranking': constants.INFO}]
        self.assertTrue(my_ptp.highest_ranking == constants.INFO)

    def test_ptp_highest_ranking_low_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [{'ranking': constants.UNKNOWN}, {'ranking': constants.INFO}, {'ranking': constants.LOW}]
        self.assertTrue(my_ptp.highest_ranking == constants.LOW)

    def test_ptp_highest_ranking_medium_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [
            {'ranking': constants.UNKNOWN}, {'ranking': constants.INFO}, {'ranking': constants.LOW},
            {'ranking': constants.MEDIUM}]
        self.assertTrue(my_ptp.highest_ranking == constants.MEDIUM)

    def test_ptp_highest_ranking_high_vuln(self):
        my_ptp = PTP()
        my_ptp.vulns = [
            {'ranking': constants.UNKNOWN}, {'ranking': constants.INFO}, {'ranking': constants.LOW},
            {'ranking': constants.MEDIUM}, {'ranking': constants.HIGH}]
        self.assertTrue(my_ptp.highest_ranking == constants.HIGH)

    def test_ptp_cumulative_parsing(self):
        my_ptp = PTP(cumulative=True)
        my_ptp.parser = MockParserInfo()  # Tool 1, first run
        report = my_ptp.parse()
        assert_that(1, equal_to(len(report)))
        assert_that(report, has_item({'ranking': constants.INFO}))
        assert_that(report, is_not(has_item({'ranking': constants.HIGH})))
        my_ptp.parser = MockParserHigh()  # Tool 2, second run
        report = my_ptp.parse()
        assert_that(2, equal_to(len(report)))
        assert_that(report, has_item({'ranking': constants.INFO}))
        assert_that(report, has_item({'ranking': constants.HIGH}))

    def test_ptp_no_cumulative_parsing(self):
        my_ptp = PTP(cumulative=False)
        my_ptp.parser = MockParserInfo()  # Tool 1, first run
        report = my_ptp.parse()
        assert_that(1, equal_to(len(report)))
        assert_that(report, has_item({'ranking': constants.INFO}))
        assert_that(report, is_not(has_item({'ranking': constants.HIGH})))
        my_ptp.parser = MockParserHigh()  # Tool 2, second run
        report = my_ptp.parse()
        assert_that(1, equal_to(len(report)))
        assert_that(report, has_item({'ranking': constants.HIGH}))
        assert_that(report, is_not(has_item({'ranking': constants.INFO})))
