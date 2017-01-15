# -*- coding: UTF-8 -*-
import os
import mock
import unittest

from ptp.libptp.parser import AbstractParser, XMLParser, FileParser, LineParser, JSONParser

from sys import version_info
if version_info.major == 2:
    import __builtin__ as builtins  # Python 2.x.
else:
    import builtins  # Python 3.x


class TestLibptpAbstractParser(unittest.TestCase):

    ###
    # AbstractParser._recursive_find
    ###
    def test_parser_abstract_init(self):
        with self.assertRaises(NotImplementedError):
            AbstractParser()

    ###
    # AbstractParser._recursive_find
    ###
    @mock.patch('os.walk', return_value=[('/foo', ('bar'), ('file1.txt')), ('/foo/bar', (), ('file2.txt'))])
    def test_parser_abstract_recursive_find_default(self, mock_os_walk):
        self.assertEqual(AbstractParser._recursive_find(), ['/foo/file1.txt'])

    @mock.patch('os.walk', return_value=[('/foo', ('bar'), ('file1.txt')), ('/foo/bar', (), ('file2.txt'))])
    def test_parser_abstract_recursive_find_first(self, mock_os_walk):
        self.assertEqual(AbstractParser._recursive_find(first=True), ['/foo/file1.txt'])

    @mock.patch('os.walk', return_value=[('/foo', ('bar'), ('file1.txt')), ('/foo/bar', (), ('file2.txt'))])
    def test_parser_abstract_recursive_find_no_first(self, mock_os_walk):
        self.assertEqual(AbstractParser._recursive_find(first=False), ['/foo/file1.txt', '/foo/bar/file2.txt'])

    @mock.patch('os.walk', return_value=[('/foo', ('bar'), ('file1.txt')), ('/foo/bar', (), ('file2.txt'))])
    def test_parser_abstract_recursive_find_regex_first(self, mock_os_walk):
        self.assertEqual(AbstractParser._recursive_find(file_regex='*file1.txt'), ['/foo/file1.txt'])

    @mock.patch('os.walk', return_value=[('/foo', ('bar'), ('file1.txt')), ('/foo/bar', (), ('file2.txt'))])
    def test_parser_abstract_recursive_find_regex_no_first(self, mock_os_walk):
        self.assertEqual(AbstractParser._recursive_find(file_regex='*file2.txt', first=False), ['/foo/bar/file2.txt'])

    ###
    # AbstractParser.handle_file
    ###
    def test_parser_abstract_handle_file(self):
        with self.assertRaises(NotImplementedError):
            AbstractParser.handle_file()

    ###
    # AbstractParser.is_mine
    ###
    def test_parser_abstract_is_mine(self):
        with self.assertRaises(NotImplementedError):
            AbstractParser.is_mine()

    ###
    # AbstractParser.check_version
    ###
    def test_parser_abstract_check_version_no_metadata(self):
        AbstractParser.__version__ = ''
        self.assertFalse(AbstractParser.check_version(metadata={}, key=None))

    def test_parser_abstract_check_version_metadata_no_key(self):
        AbstractParser.__version__ = ''
        self.assertFalse(AbstractParser.check_version(metadata={'version': '123'}, key=None))

    def test_parser_abstract_check_version_metadata_with_key(self):
        AbstractParser.__version__ = ''
        self.assertFalse(AbstractParser.check_version(metadata={'version': '123'}, key='version'))

    def test_parser_abstract_check_version_metadata_with_key_default(self):
        AbstractParser.__version__ = ''
        self.assertFalse(AbstractParser.check_version(metadata={'version': '123'}))

    def test_parser_abstract_check_version_metadata_with_key_default_with_match(self):
        AbstractParser.__version__ = '123'
        self.assertTrue(AbstractParser.check_version(metadata={'version': r'123'}))

    ###
    # AbstractParser.parse_metadata
    ###
    def test_parser_abstract_parse_metadata(self):
        with self.assertRaises(NotImplementedError):
            AbstractParser().parse_metadata()

    ###
    # AbstractParser.parse_report
    ###
    def test_parser_abstract_parse_report(self):
        with self.assertRaises(NotImplementedError):
            AbstractParser().parse_report()


class TestLibptpXMLParser(unittest.TestCase):

    ###
    # XMLParser.handle_file
    ###
    @mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=[])
    def test_parser_xml_handle_file_no_file(self, mock_recursive_find):
        with self.assertRaises(IOError):
            XMLParser.handle_file('/dev/null')

    @mock.patch('ptp.libptp.parser.XMLParser._recursive_find', return_value=['test.txt'])
    def test_parser_xml_handle_file_wrong_extension(self, mock_recursive_find):
        XMLParser.__format__ = '.xml'
        with self.assertRaises(TypeError):
            XMLParser.handle_file('/dev/null')


class TestLibptpFileParser(unittest.TestCase):

    ###
    # FileParser.__init__
    ###
    @mock.patch('ptp.libptp.parser.FileParser._recursive_find', return_value=[])
    def test_parser_file_init_no_file(self, mock_recursive_find):
        with self.assertRaises(IOError):
            FileParser(pathname='/dev/', filename='null')

    @mock.patch('ptp.libptp.parser.FileParser._recursive_find', return_value=['test.txt'])
    def test_parser_file_init_with_content(self, mock_recursive_find):
        try:
            str_type = basestring  # Python 2.x.
        except NameError:
            str_type = str  # Python 3.x.
        with mock.patch.object(builtins, 'open', mock.mock_open(read_data='The cake is a lie!\nThe cake is a lie!')):
            my_fileparser = FileParser(pathname='./', filename='text.txt')
            self.assertIsInstance(my_fileparser.stream, str_type)
            self.assertTrue(my_fileparser.stream == 'The cake is a lie!\nThe cake is a lie!')

    ###
    # FileParser.handle_file
    ###
    @mock.patch('ptp.libptp.parser.FileParser._recursive_find', return_value=[])
    def test_parser_file_handle_file_no_file(self, mock_recursive_find):
        with self.assertRaises(IOError):
            FileParser.handle_file('/dev/null')

    @mock.patch('ptp.libptp.parser.FileParser._recursive_find', return_value=['test.txt'])
    def test_parser_file_handle_file_with_content(self, mock_recursive_find):
        try:
            str_type = basestring  # Python 2.x.
        except NameError:
            str_type = str  # Python 3.x.
        with mock.patch.object(builtins, 'open', mock.mock_open(read_data='The cake is a lie!\nThe cake is a lie!')):
            data = FileParser.handle_file('text.txt')
            self.assertIsInstance(data, str_type)
            self.assertTrue(data == 'The cake is a lie!\nThe cake is a lie!')


class TestLibptpLineParser(unittest.TestCase):

    # FIXME: Use random name. One function exists in python for that but in the train ATM so can't look it up.
    OPEN_FILE = '/tmp/test_ptp_open'

    def setUp(self):
        with open(self.OPEN_FILE, 'w') as f:
            f.write('The cake is a lie!\n\nThe cake is a lie!')

    def tearDown(self):
        if os.path.exists(self.OPEN_FILE) and os.path.isfile(self.OPEN_FILE):
            os.remove(self.OPEN_FILE)

    ###
    # LineParser.__init__
    ###
    @mock.patch('ptp.libptp.parser.LineParser._recursive_find', return_value=[])
    def test_parser_line_init_no_file(self, mock_recursive_find):
        with self.assertRaises(IOError):
            LineParser(pathname='/dev/', filename='null')

    @mock.patch('ptp.libptp.parser.FileParser._recursive_find', return_value=['test.txt'])
    def test_parser_line_init_with_content(self, mock_recursive_find):
        my_lineparser = LineParser(pathname='/tmp/', filename='test_ptp_open')
        self.assertIsInstance(my_lineparser.stream, list)
        self.assertTrue(my_lineparser.stream == ['The cake is a lie!', 'The cake is a lie!'])

    ###
    # LineParser.handle_file
    ###
    @mock.patch('ptp.libptp.parser.LineParser._recursive_find', return_value=[])
    def test_parser_line_handle_file_no_file(self, mock_recursive_find):
        with self.assertRaises(IOError):
            LineParser.handle_file('/dev/null')

    def test_parser_line_handle_file_with_content(self):
        # No Skip Empty
        data = LineParser.handle_file(pathname='/tmp/', filename='test_ptp_open', skip_empty=False)
        self.assertIsInstance(data, list)
        self.assertTrue(data == ['The cake is a lie!', '', 'The cake is a lie!'])
        # Skip empty
        data = LineParser.handle_file(pathname='/tmp/', filename='test_ptp_open', skip_empty=True)
        self.assertIsInstance(data, list)
        self.assertTrue(data == ['The cake is a lie!', 'The cake is a lie!'])


class TestLibptpJSONParser(unittest.TestCase):

    ###
    # JSON.handle_file
    ###
    @mock.patch('ptp.libptp.parser.JSONParser._recursive_find', return_value=[])
    def test_parser_json_handle_file_no_file(self, mock_recursive_find):
        with self.assertRaises(IOError):
            JSONParser.handle_file('/dev/null')

    @mock.patch('ptp.libptp.parser.JSONParser._recursive_find', return_value=['test.txt'])
    def test_parser_json_handle_file_wrong_extension(self, mock_recursive_find):
        JSONParser.__format__ = '.json'
        with self.assertRaises(TypeError):
            JSONParser.handle_file('/dev/null')

    @mock.patch('ptp.libptp.parser.JSONParser._recursive_find', return_value=['test.json'])
    def test_parser_json_handle_file_invalid_json(self, mock_recursive_find):
        JSONParser.__format__ = '.json'
        with mock.patch.object(builtins, 'open', mock.mock_open(read_data='The cake is a lie!\nThe cake is a lie!')):
            with self.assertRaises(ValueError):
                JSONParser.handle_file('/dev/null')

    @mock.patch('ptp.libptp.parser.JSONParser._recursive_find', return_value=['test.json'])
    def test_parser_json_handle_file_valid_json(self, mock_recursive_find):
        JSONParser.__format__ = '.json'
        with mock.patch.object(builtins, 'open', mock.mock_open(read_data='{"test": true}')):
            data = JSONParser.handle_file('/dev/null')
            self.assertTrue(data == {'test': True})
