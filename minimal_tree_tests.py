import unittest

from minimal_tree import minimal_tree
from tree_node import TreeNode


class BuildMinimalTreeTests(unittest.TestCase):

    def test_single_node(self):
        self.assertEqual(
            minimal_tree([1]),
            TreeNode(1)
        )

    def test_minimal_tree_simple(self):
        expected = TreeNode(2)
        expected.left = TreeNode(1)
        expected.right = TreeNode(3)

        self.assertEqual(
            minimal_tree([1, 2, 3]),
            expected
        )
