import unittest

from palindrome_permutation import Solution


class PanindromePermutationTests(unittest.TestCase):

    def test_palindrome_permutation(self):
        self.assertTrue(Solution().palindrome_permutation('Race car'))
        self.assertFalse(Solution().palindrome_permutation('Race carm'))
        self.assertTrue(Solution().palindrome_permutation('Tact coa'))
