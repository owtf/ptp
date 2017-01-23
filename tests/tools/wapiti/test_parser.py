# -*- coding: UTF-8 -*-
import mock
import unittest

from lxml import etree
from hamcrest import assert_that, has_entry, has_item, has_items, is_not

from ptp.libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH
from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.tools.wapiti.parser import WapitiXMLParser


def lxml_etree_parse(string):
    return etree.fromstring(string).getroottree()


class TestWapitiXMLParser(unittest.TestCase):

    ###
    # WapitiXMLParser.is_mine
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_wapiti_xml_is_mine(self, mock_lxml_etree_parse):
        from .wapiti_reports_2_3_0 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            WapitiXMLParser.__format__ = ''
            self.assertTrue(WapitiXMLParser.is_mine('foo', 'bar', first=True))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_wapiti_xml_is_not_mine(self, mock_lxml_etree_parse):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=['foo.bar']):
            WapitiXMLParser.__format__ = ''
            self.assertFalse(WapitiXMLParser.is_mine('foo', 'bar', first=True))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_wapiti_xml_is_mine_no_version(self, mock_lxml_etree_parse):
        from .wapiti_reports_2_3_0 import report_high
        stripped_report = report_high.replace('"generatorVersion"', '"generatorINVALIDHEADER"')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[stripped_report]):
            WapitiXMLParser.__format__ = ''
            self.assertFalse(WapitiXMLParser.is_mine('foo', 'bar', first=True))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_wapiti_xml_is_mine_version_not_supported(self, mock_lxml_etree_parse):
        from .wapiti_reports_2_3_0 import report_high
        stripped_report = report_high.replace('Wapiti 2.3.0', 'Wapiti VERSIONTHATWONTEVEREXIST')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[stripped_report]):
            WapitiXMLParser.__format__ = ''
            self.assertFalse(WapitiXMLParser.is_mine('foo', 'bar', first=True))

    ###
    # WapitiXMLParser.parse_metadata
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_wapiti_xml_parse_metadata(self, mock_lxml_etree_parse):
        from .wapiti_reports_2_3_0 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            WapitiXMLParser.__format__ = ''
            my_wapiti = WapitiXMLParser('foo', 'bar', first=True)
            assert_that(my_wapiti.parse_metadata(), has_entry('generatorVersion', '2.3.0'))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_wapiti_xml_parse_metadata_version_not_supported(self, mock_lxml_etree_parse):
        from .wapiti_reports_2_3_0 import report_high
        stripped_report = report_high.replace('Wapiti 2.3.0', 'Wapiti VERSIONTHATWONTEVEREXIST')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[stripped_report]):
            WapitiXMLParser.__format__ = ''
            my_wapiti = WapitiXMLParser('foo', 'bar', first=True)
            with self.assertRaises(NotSupportedVersionError):
                my_wapiti.parse_metadata()

    ###
    # WapitiXMLParser.parse_report
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_wapiti_xml_parse_report(self, mock_lxml_etree_parse):
        from .wapiti_reports_2_3_0 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            WapitiXMLParser.__format__ = ''
            my_wapiti = WapitiXMLParser()
            report = my_wapiti.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH, 'name': 'Cross Site Scripting', 'description': '\nCross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications which allow code injection by malicious web users into the web pages viewed by other users. Examples of such code include HTML code and client-side scripts.            '}] * 1))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
