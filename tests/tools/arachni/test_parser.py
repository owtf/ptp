# -*- coding: UTF-8 -*-
import mock
import json
import unittest

from lxml import etree
from hamcrest import assert_that, has_entry, has_item, has_items, is_not, equal_to

from ptp.libptp.constants import UNKNOWN, INFO, LOW, MEDIUM, HIGH
from ptp.libptp.exceptions import NotSupportedVersionError
from ptp.tools.arachni.parser import ArachniXMLParser, ArachniJSONParser


def lxml_etree_parse(string):
    return etree.fromstring(string).getroottree()


def handle_json_file(string, *args, **kwargs):
    return json.loads(string)


class TestArachniXMLParser(unittest.TestCase):

    ###
    # ArachniXMLParser.is_mine
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_is_mine(self, mock_lxml_etree_parse):
        # Arachni version 1.0
        from .arachni_reports_1_0 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        from .arachni_reports_1_0 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        # Arachni version 1.0.1
        from .arachni_reports_1_0_1 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        from .arachni_reports_1_0_1 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        # Arachni version 1.0.2
        from .arachni_reports_1_0_2 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        from .arachni_reports_1_0_2 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        # Arachni version 1.0.3
        from .arachni_reports_1_0_3 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        from .arachni_reports_1_0_3 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        # Arachni version 1.0.4
        from .arachni_reports_1_0_4 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        from .arachni_reports_1_0_4 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        # Arachni version 1.0.5
        from .arachni_reports_1_0_5 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        from .arachni_reports_1_0_5 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        # Arachni version 1.0.6
        from .arachni_reports_1_0_6 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        from .arachni_reports_1_0_6 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        # Arachni version 1.1
        from .arachni_reports_1_1 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        from .arachni_reports_1_1 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))
        # Arachni version 1.2.1
        from .arachni_reports_1_2_1 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            self.assertTrue(ArachniXMLParser.is_mine('foo', 'bar', first=True))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_is_not_mine(self, mock_lxml_etree_parse):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=['foo.bar']):
            ArachniXMLParser.__format__ = ''
            self.assertFalse(ArachniXMLParser.is_mine('foo', 'bar', first=True))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_is_mine_but_no_version(self, mock_lxml_etree_parse):
        from .arachni_reports_1_2_1 import report_high
        stripped_report = report_high.replace('<version>', '<notversionanymore>').replace('</version>', '</notversionanymore>')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[stripped_report]):
            ArachniXMLParser.__format__ = ''
            self.assertFalse(ArachniXMLParser.is_mine('foo', 'bar', first=True))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_is_mine_but_unsupported_version(self, mock_lxml_etree_parse):
        from .arachni_reports_1_2_1 import report_high
        stripped_report = report_high.replace('<version>1.2.1</version>', '<version>INVALIDVERSIONNEVERWILLITHAPPEN</version>')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[stripped_report]):
            ArachniXMLParser.__format__ = ''
            self.assertFalse(ArachniXMLParser.is_mine('foo', 'bar', first=True))

    ###
    # ArachniXMLParser.parse_metadata
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_parse_metadata(self, mock_lxml_etree_parse):
        # Arachni version 1.0
        from .arachni_reports_1_0 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0'))
        from .arachni_reports_1_0 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0'))
        # Arachni version 1.0.1
        from .arachni_reports_1_0_1 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.1'))
        from .arachni_reports_1_0_1 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.1'))
        # Arachni version 1.0.2
        from .arachni_reports_1_0_2 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.2'))
        from .arachni_reports_1_0_2 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.2'))
        # Arachni version 1.0.3
        from .arachni_reports_1_0_3 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.3'))
        from .arachni_reports_1_0_3 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.3'))
        # Arachni version 1.0.4
        from .arachni_reports_1_0_4 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.4'))
        from .arachni_reports_1_0_4 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.4'))
        # Arachni version 1.0.5
        from .arachni_reports_1_0_5 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.5'))
        from .arachni_reports_1_0_5 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.5'))
        # Arachni version 1.0.6
        from .arachni_reports_1_0_6 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.6'))
        from .arachni_reports_1_0_6 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.0.6'))
        # Arachni version 1.1
        from .arachni_reports_1_1 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.1'))
        from .arachni_reports_1_1 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            assert_that(my_arachni.parse_metadata(), has_entry('version', '1.1'))

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_parse_metadata_unsupported_version(self, mock_lxml_etree_parse):
        from .arachni_reports_1_2_1 import report_high
        stripped_report = report_high.replace('<version>1.2.1</version>', '<version>INVALIDVERSIONNEVERWILLITHAPPEN</version>')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[stripped_report]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            with self.assertRaises(NotSupportedVersionError):
                my_arachni.parse_metadata()

    ###
    # ArachniXMLParser.parse_report
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_parse_report(self, mock_lxml_etree_parse):
        # Arachni version 1.0
        from .arachni_reports_1_0 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 3))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .arachni_reports_1_0 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, has_items(*[{'ranking': LOW}] * 2))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        # Arachni version 1.0.1
        from .arachni_reports_1_0_1 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 3))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .arachni_reports_1_0_1 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, has_items(*[{'ranking': LOW}] * 2))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        # Arachni version 1.0.2
        from .arachni_reports_1_0_2 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 3))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .arachni_reports_1_0_2 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, has_items(*[{'ranking': LOW}] * 2))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        # Arachni version 1.0.3
        from .arachni_reports_1_0_3 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 3))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .arachni_reports_1_0_3 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, has_items(*[{'ranking': LOW}] * 2))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        # Arachni version 1.0.4
        from .arachni_reports_1_0_4 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 3))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .arachni_reports_1_0_4 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, has_items(*[{'ranking': LOW}] * 2))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        # Arachni version 1.0.5
        from .arachni_reports_1_0_5 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 3))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .arachni_reports_1_0_5 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, has_items(*[{'ranking': LOW}] * 2))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        # Arachni version 1.0.6
        from .arachni_reports_1_0_6 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 3))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .arachni_reports_1_0_6 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, has_items(*[{'ranking': LOW}] * 2))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        # Arachni version 1.1
        from .arachni_reports_1_1 import report_low
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_low]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': LOW}] * 3))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
            assert_that(report, is_not(has_item([{'ranking': HIGH}])))
        from .arachni_reports_1_1 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': HIGH}] * 4))
            assert_that(report, has_items(*[{'ranking': LOW}] * 2))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(report, is_not(has_item([{'ranking': INFO}])))
            assert_that(report, is_not(has_item([{'ranking': MEDIUM}])))
        # Arachni version 1.2.1
        from .arachni_reports_1_2_1 import report_high
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_high]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            report = my_arachni.parse_report()
            assert_that(report, has_items(*[{'ranking': INFO}] * 6))
            assert_that(report, has_item(*[{'ranking': MEDIUM}]))
            assert_that(report, has_item(*[{'ranking': LOW}]))
            assert_that(report, has_item(*[{'ranking': HIGH}]))
            assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
            assert_that(10, equal_to(len(report)))
            assert_that(10, equal_to(len(report[-1]['transactions'])))

class TestArachniJSONParser(unittest.TestCase):

    ###
    # ArachniJSONParser.is_mine
    ###
    @mock.patch('ptp.libptp.parser.JSONParser.handle_file', side_effect=handle_json_file)
    def test_parser_arachni_json_is_mine(self, mock_handle):
        # Arachni version 1.2.1
        from .arachni_json_reports_1_2_1 import report_high
        ArachniJSONParser.__format__ = ''
        self.assertTrue(ArachniJSONParser.is_mine(report_high, first=True))

    @mock.patch('ptp.libptp.parser.JSONParser.handle_file', side_effect=handle_json_file)
    def test_parser_arachni_json_is_not_mine(self, mock_handle):
        ArachniJSONParser.__format__ = ''
        self.assertFalse(ArachniJSONParser.is_mine('foo', first=True))

    @mock.patch('ptp.libptp.parser.JSONParser.handle_file', side_effect=handle_json_file)
    def test_parser_arachni_json_is_mine_but_no_version(self, mock_handle):
        from .arachni_json_reports_1_2_1 import report_high
        stripped_report = report_high.replace('"version"', '"notversionanymore"')
        ArachniJSONParser.__format__ = ''
        self.assertFalse(ArachniJSONParser.is_mine(stripped_report, first=True))

    @mock.patch('ptp.libptp.parser.JSONParser.handle_file', side_effect=handle_json_file)
    def test_parser_arachni_json_is_mine_but_unsupported_version(self, mock_handle):
        from .arachni_json_reports_1_2_1 import report_high
        stripped_report = report_high.replace('"version" : "1.2.1"', '"version" : "INVALIDVERSIONNEVERWILLITHAPPEN"')
        ArachniJSONParser.__format__ = ''
        self.assertFalse(ArachniJSONParser.is_mine(stripped_report, first=True))

    ###
    # ArachniJSONParser.parse_metadata()
    ###
    @mock.patch('ptp.libptp.parser.JSONParser.handle_file', return_value={})
    def test_parser_arachni_json_parse_metadata(self, mock_handle):
        # Arachni version 1.2.1
        from .arachni_json_reports_1_2_1 import report_high
        my_arachni = ArachniJSONParser(None)
        my_arachni.stream = json.loads(report_high)
        report = my_arachni.parse_metadata()
        assert_that(report, has_entry("version", "1.2.1"))

    @mock.patch('ptp.libptp.parser.JSONParser.handle_file', return_value={})
    def test_parser_arachni_json_parse_metadata_unsupported_version(self, mock_handle):
        from .arachni_json_reports_1_2_1 import report_high
        stripped_report = report_high.replace('"version" : "1.2.1"', '"version" : "INVALIDVERSIONNEVERWILLITHAPPEN"')
        ArachniJSONParser.__format__ = ''
        my_arachni = ArachniJSONParser(None)
        my_arachni.stream = json.loads(stripped_report)
        with self.assertRaises(NotSupportedVersionError):
            my_arachni.parse_metadata()

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_arachni_xml_parse_metadata_unsupported_version(self, mock_lxml_etree_parse):
        from .arachni_reports_1_2_1 import report_high
        stripped_report = report_high.replace('<version>1.2.1</version>', '<version>INVALIDVERSIONNEVERWILLITHAPPEN</version>')
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[stripped_report]):
            ArachniXMLParser.__format__ = ''
            my_arachni = ArachniXMLParser('foo', 'bar', first=True)
            with self.assertRaises(NotSupportedVersionError):
                my_arachni.parse_metadata()

    ###
    # ArachniJSONParser.parse_report
    ###
    @mock.patch('ptp.libptp.parser.JSONParser.handle_file', return_value={})
    def test_parser_arachni_json_parse_report(self, mock_handle):
        # Arachni version 1.2.1
        from .arachni_json_reports_1_2_1 import report_high
        my_arachni = ArachniJSONParser(None)
        my_arachni.stream = json.loads(report_high)
        report = my_arachni.parse_report()
        assert_that(report, has_items(*[{'ranking': INFO}] * 6))
        assert_that(report, has_item(*[{'ranking': MEDIUM}]))
        assert_that(report, has_item(*[{'ranking': LOW}]))
        assert_that(report, has_item(*[{'ranking': HIGH}]))
        assert_that(report, is_not(has_item([{'ranking': UNKNOWN}])))
        assert_that(10, equal_to(len(report)))
        assert_that(10, equal_to(len(report[-1]['transactions'])))
