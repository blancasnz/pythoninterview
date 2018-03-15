

class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        if not other:
            return False

        if self.val != other.val:
            return False

        return self.left == other.left and self.right == other.right
