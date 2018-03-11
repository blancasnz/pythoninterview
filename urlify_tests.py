import unittest

from urlify import Solution


class UniqueTests(unittest.TestCase):

    def test_urlify(self):
        self.assertEquals(Solution().urlify('a b c '), 'a%20b%20c%20')
