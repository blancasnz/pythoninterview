import unittest

from compression import Solution


class CompressionTests(unittest.TestCase):

    def test_compression(self):
        input = ['a', 'a', 'b', 'b']

        result = Solution().compress(input)

        self.assertEqual(result, 'a2b2')

    def test_compression_1(self):
        input = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

        result = Solution().compress(input)

        self.assertEqual(result, 'ab10')
