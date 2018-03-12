import unittest

from spiral_matrix import spiral_matrix


class SpiralMatrixTests(unittest.TestCase):

    def test_4x4(self):
        expected = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
        self.assertEqual(spiral_matrix(4), expected)

    def test_5x5(self):
        expected = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        self.assertEqual(spiral_matrix(5), expected)
