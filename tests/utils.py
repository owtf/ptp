class MockParser(object):

    __tool__ = 'mock'

    def __init__(self):
        pass

    def parse_metadata(self):
        return {}

    def parse_report(self):
        return []
