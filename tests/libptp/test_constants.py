# -*- coding: UTF-8 -*-
import unittest

from ptp.libptp import constants


class TestLibptpConstants(unittest.TestCase):

    ###
    # constants.UNKNOWN
    ###
    def test_constants_unknown(self):
        self.assertTrue(constants.UNKNOWN == 0)

    ###
    # constants.INFO
    ###
    def test_constants_info(self):
        self.assertTrue(constants.INFO == 1)

    ###
    # constants.LOW
    ###
    def test_constants_low(self):
        self.assertTrue(constants.LOW == 2)

    ###
    # constants.MEDIUM
    ###
    def test_constants_medium(self):
        self.assertTrue(constants.MEDIUM == 3)

    ###
    # constants.HIGH
    ###
    def test_constants_high(self):
        self.assertTrue(constants.HIGH == 4)

    ###
    # constants.RANKING_SCALE
    ###
    def test_constants_ranking_scale(self):
        self.assertTrue(constants.RANKING_SCALE == {0: 0, 1: 1, 2: 2, 3: 3, 4: 4})
