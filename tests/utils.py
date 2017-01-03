from ptp.libptp import constants


class MockParser(object):

    __tool__ = 'mock'

    def __init__(self):
        pass

    def parse_metadata(self):
        return {}

    def parse_report(self):
        return []


class MockParserInfo(MockParser):

    __tool__ = 'mock_info'

    def parse_report(self):
        return [{'ranking': constants.INFO}]


class MockParserHigh(MockParser):

    __tool__ = 'mock_high'

    def parse_report(self):
        return [{'ranking': constants.HIGH}]
