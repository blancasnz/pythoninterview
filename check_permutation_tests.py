import unittest

from check_permutation import Solution


class UniqueTests(unittest.TestCase):

    def test_is_permutation(self):
        self.assertTrue(Solution().is_permutation('hello', 'lloeh'))
        self.assertFalse(Solution().is_permutation('hello', 'hell'))
        self.assertTrue(Solution().is_permutation('HELLO', 'olleh'))
