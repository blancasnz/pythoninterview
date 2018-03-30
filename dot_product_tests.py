import unittest

import dot_product as dp


class DotProductTests(unittest.TestCase):

    def test_compression(self):
        result = dp.compress_sparse_matrix([0, 0, 0, 0, 9, 0, 0])
        self.assertEqual(result, ["04", "9", "02"])

    def test_dot_product_sparse(self):
        compress_a = ["04", "4", "03"]
        compress_b = ["02", "5", "01", "1", "03"]

        result = dp.sparse_dot_product(compress_a, compress_b)

        self.assertEqual(result, 4)

    def test_dot_product(self):
        a = [0, 0, 0, 0, 4, 0, 0, 0]
        b = [0, 0, 5, 0, 1, 0, 0, 0]

        result = dp.dot_product(a, b)

        self.assertEqual(result, 4)
