import math

from tree_node import TreeNode


def minimal_tree(input):
    """
    Given list of sorted numbers. Create a binary tree
    with minimal height.
    """

    def build(start, end):
        if end < start:
            return

        mid = math.ceil((end - start) / 2) + start

        root = TreeNode(input[mid])
        root.left = build(start, mid - 1)
        root.right = build(mid + 1, end)
        return root

    return build(0, len(input) - 1)
