from ptp.libptp import constants


class MockParser(object):

    __tool__ = 'mock'

    def __init__(self):
        self.stream = ''

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
