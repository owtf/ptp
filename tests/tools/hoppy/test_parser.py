# -*- coding: UTF-8 -*-
import mock
import unittest

from hamcrest import assert_that, has_entry, equal_to

from ptp.tools.hoppy.parser import HoppyParser

class TestHoppyParser(unittest.TestCase):

    ###
    # HoppyParser.is_mine
    ###
    def test_parser_hoppy_is_mine(self):
        self.assertTrue(HoppyParser.is_mine('./'))

    ###
    # HoppyParser.parse_metadata
    ###
    def test_parser_hoppy_parse_metadata(self):
        my_hoppy = HoppyParser('./')
        assert_that(my_hoppy.parse_metadata(), has_entry('version', '1.8.1'))

    ###
    # HoppyParser.parse_report
    ###
    def test_parser_burp_xml_parse_report(self):
        HoppyParser.__format__ = ''
        my_hoppy = HoppyParser("./")
        report = my_hoppy.parse_report()
        assert_that(4, equal_to(len(report[-1]['transactions'])))