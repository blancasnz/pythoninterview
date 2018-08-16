class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def merge_trees(t1, t2):
    if not t1 and not t2:
        return None

    if t1 and t2:
        root = TreeNode(t1.val + t2.val)
        left = merge_trees(t1.left, t2.left)
        right = merge_trees(t1.right, t2.right)
    elif t1:
        root = TreeNode(t1.val)
        left = merge_trees(t1.left, None)
        right = merge_trees(t1.right, None)
    elif t2:
        root = TreeNode(t2.val)
        left = merge_trees(None, t2.left)
        right = merge_trees(None, t2.right)

    root.left = left
    root.right = right

    return root
