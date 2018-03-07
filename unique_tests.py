import unittest

from unique import Solution


class UniqueTests(unittest.TestCase):

    def test_is_unique(self):

        self.assertTrue(Solution().is_unique(''))
        self.assertFalse(Solution().is_unique('abca'))
        self.assertFalse(Solution().is_unique('abcA'))
        self.assertTrue(Solution().is_unique(None))
