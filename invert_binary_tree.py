
def invert_tree(root):
    if not root:
        return root

    temp = invert_tree(root.right)
    root.right = invert_tree(root.left)
    root.left = temp

    return root
