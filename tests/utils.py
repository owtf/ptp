from ptp.libptp import constants
from ptp.libptp.exceptions import NotSupportedVersionError


class MockParser(object):

    __tool__ = 'mock'

    def __init__(self):
        self.stream = ''

    @classmethod
    def is_mine(cls, *args, **kwargs):
        return True

    def parse_metadata(self):
        return {}

    def parse_report(self):
        return []


class MockParserVersionNotSupported(MockParser):

    __tool__ = 'mock_invalid_version'

    @classmethod
    def is_mine(cls, *args, **kwargs):
        raise NotSupportedVersionError('PTP does NOT support this version of mock_invalid_version.')


class MockParserIOError(MockParser):

    __tool__ = 'mock_ioerror'

    @classmethod
    def is_mine(cls, *args, **kwargs):
        raise IOError


class MockParserInfo(MockParser):

    __tool__ = 'mock_info'

    def parse_report(self):
        return [{'ranking': constants.INFO}]


class MockParserHigh(MockParser):

    __tool__ = 'mock_high'

    def parse_report(self):
        return [{'ranking': constants.HIGH}]


class MockParserLight(MockParser):

    ___tool__ = 'mock_light'

    def __init__(self, light=True):
        self.light = light
        MockParser.__init__(self)

    @classmethod
    def handle_file(cls, light=True):
        return ''

    @classmethod
    def is_mine(cls, light=True):
        return True

    def parse_metadata(self):
        return {}

    def parse_report(self):
        vulns = []
        if not self.light:  # More complete parsing
            vulns = [{'ranking': constants.UNKNOWN, 'transactions': [{'request': '', 'response': ''}]}]
        return vulns
