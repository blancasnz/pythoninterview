import unittest

from lettercase_permutation import Solution


class LetterCasePermutation(unittest.TestCase):

    def test_lettercase_permutation(self):
        input = 'a1b2'

        result = Solution().letter_case_permutation(input)

        self.assertEqual(result, set(['a1b2', 'A1b2', 'a1B2', 'A1B2']))

    def test_lettercase_permutation_numbers(self):
        input = '1234'

        result = Solution().letter_case_permutation(input)

        self.assertEqual(result, set(['1234']))
