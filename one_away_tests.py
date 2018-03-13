import unittest

from one_away import one_away, one_away_v2


class OneAwayTests(unittest.TestCase):

    def test_one_away(self):
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertFalse(one_away('pale', 'bake'))

    def test_one_away_v2(self):
        self.assertTrue(one_away_v2('pale', 'ple'))
        self.assertTrue(one_away_v2('pales', 'pale'))
        self.assertTrue(one_away_v2('pale', 'bale'))
        self.assertFalse(one_away_v2('pale', 'bake'))
