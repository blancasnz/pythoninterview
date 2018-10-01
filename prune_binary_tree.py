

def prune_binary_tree(root):
    if not root:
        return root

    if not contains_one(root.left):
        root.left = None
    if not contains_one(root.right):
        root.right = None

    prune_binary_tree(root.left)
    prune_binary_tree(root.right)
    return root


def contains_one(root):
    if not root:
        return False
    if root.val == 1:
        return True
    return contains_one(root.left) or contains_one(root.right)
