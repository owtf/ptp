# -*- coding: UTF-8 -*-
import mock
import unittest

from lxml import etree
from hamcrest import assert_that, has_entry, has_item, has_items, is_not, equal_to

from ptp.libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH
from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.tools.w3af.parser import W3AFXMLParser


def lxml_etree_parse(string):
    return etree.fromstring(string).getroottree()


class TestW3AFXMLParser(unittest.TestCase):

    ###
    # W3AFXMLParser.is_mine
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_w3af_xml_is_mine(self, mock_lxml_etree_parse):
        # W3AF version 1.6.0.2
        from .w3af_reports_1_6_0_2 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        # W3AF version 1.6.0.3
        from .w3af_reports_1_6_0_3 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        from .w3af_reports_1_6_0_3 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        # W3AF version 1.6.0.5
        from .w3af_reports_1_6_0_5 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        from .w3af_reports_1_6_0_5 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        # W3AF version 1.6.45
        from .w3af_reports_1_6_45 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        from .w3af_reports_1_6_45 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        # W3AF version 1.6.46
        from .w3af_reports_1_6_46 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        from .w3af_reports_1_6_46 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        # W3AF version 1.6.49
        from .w3af_reports_1_6_49 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        from .w3af_reports_1_6_49 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        # W3AF version 1.6.50
        from .w3af_reports_1_6_50 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        from .w3af_reports_1_6_50 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        # W3AF version 1.6.51
        from .w3af_reports_1_6_51 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        from .w3af_reports_1_6_51 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_w3af_xml_is_not_mine(self, mock_lxml_etree_parse):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=['foo.bar']):
            W3AFXMLParser.__format__ = ''
            self.assertFalse(W3AFXMLParser.is_mine('foo', 'bar', first=True))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_w3af_xml_is_mine_no_version(self, mock_lxml_etree_parse):
        from .w3af_reports_1_6_51 import report_medium
        report_medium = report_medium.replace('w3af-version', 'foo-bar')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertFalse(W3AFXMLParser.is_mine('foo', 'bar', first=True))
        # W3AF report without version specified
        from .w3af_reports_invalid import report_no_version
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_no_version]):
            W3AFXMLParser.__format__ = ''
            self.assertTrue(W3AFXMLParser.is_mine('foo', 'bar', first=True) == False)

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_w3af_xml_is_mine_unsupported_version(self, mock_lxml_etree_parse):
        from .w3af_reports_1_6_51 import report_medium
        report_medium = report_medium.replace('1.6.51', 'foo.bar')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            self.assertFalse(W3AFXMLParser.is_mine('foo', 'bar', first=True))

    ###
    # W3AFXMLParser.parse_metadata
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_w3af_xml_parse_metadata(self, mock_lxml_etree_parse):
        # W3AF version 1.6.0.2
        from .w3af_reports_1_6_0_2 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.0.2'))
        # W3AF version 1.6.0.3
        from .w3af_reports_1_6_0_3 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.0.3'))
        from .w3af_reports_1_6_0_3 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.0.3'))
        # W3AF version 1.6.0.5
        from .w3af_reports_1_6_0_5 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.0.5'))
        from .w3af_reports_1_6_0_5 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.0.5'))
        # W3AF version 1.6.45
        from .w3af_reports_1_6_45 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.45'))
        from .w3af_reports_1_6_45 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.45'))
        # W3AF version 1.6.46
        from .w3af_reports_1_6_46 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.46'))
        from .w3af_reports_1_6_46 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.46'))
        # W3AF version 1.6.49
        from .w3af_reports_1_6_49 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.49'))
        from .w3af_reports_1_6_49 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.49'))
        # W3AF version 1.6.50
        from .w3af_reports_1_6_50 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.49'))
        from .w3af_reports_1_6_50 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.49'))
        # W3AF version 1.6.51
        from .w3af_reports_1_6_51 import report_medium
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.51'))
        from .w3af_reports_1_6_51 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            assert_that(my_w3af.parse_metadata(), has_entry('version', '1.6.51'))
        # W3AF unsupported version
        from .w3af_reports_1_6_51 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            with mock.patch('ptp.libptp.parser.AbstractParser.check_version', return_value=False):
                with self.assertRaises(NotSupportedVersionError):
                    W3AFXMLParser.__format__ = ''
                    my_w3af = W3AFXMLParser('foo', 'bar', first=True)
                    my_w3af.parse_metadata()

    ###
    # ArachniXMLParser.parse_report
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_parse_report(self, mock_lxml_etree_parse):
        # W3AF version 1.6.0.2
        from .w3af_reports_1_6_0_2 import report_high
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 7))
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 9))
            assert_that(report, has_items(*[{'ranking': HIGH}] * 14))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
        # W3AF version 1.6.0.3
        from .w3af_reports_1_6_0_3 import report_medium
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .w3af_reports_1_6_0_3 import report_high
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 3))
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
        # W3AF version 1.6.0.5
        from .w3af_reports_1_6_0_5 import report_medium
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .w3af_reports_1_6_0_5 import report_high
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 3))
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
        # W3AF version 1.6.45
        from .w3af_reports_1_6_45 import report_medium
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .w3af_reports_1_6_45 import report_high
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 3))
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
        # W3AF version 1.6.46
        from .w3af_reports_1_6_46 import report_medium
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .w3af_reports_1_6_46 import report_high
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 3))
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
        # W3AF version 1.6.49
        from .w3af_reports_1_6_49 import report_medium
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .w3af_reports_1_6_49 import report_high
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 3))
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
        # W3AF version 1.6.50
        from .w3af_reports_1_6_50 import report_medium
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .w3af_reports_1_6_50 import report_high
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_high]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 3))
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
        # W3AF version 1.6.51
        from .w3af_reports_1_6_51 import report_medium
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_medium]):
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            report = my_w3af.parse_report()
            assert_that(report, has_items(*[{'ranking': MEDIUM}] * 5))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': LOW}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))

    ###
    # ArachniXMLParser._parse_report_full
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_parse_report_http(self, mock_lxml_etree_parse):
        from .w3af_http_reports_1_6_51 import report_http
        from .w3af_reports_1_6_51 import report_medium
        with mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[report_medium]):
            # W3AF version 1.6.51 with HTTP report
            W3AFXMLParser.__format__ = ''
            my_w3af = W3AFXMLParser('foo', 'bar', first=True)
            transactions = my_w3af._parse_report_full(report_http)
            # XML parsing should be OK since tested just above so we only check HTTP transactions.
            self.assertTrue(transactions and len(transactions))  # Not empty and contain at least one element
            transaction = transactions[0]  # Only check one transaction.
            self.assertTrue(transaction.get('request', False))
            self.assertTrue(transaction.get('status_code', False))
            self.assertTrue(transaction.get('headers', False))
            self.assertTrue(transaction.get('body', False))
