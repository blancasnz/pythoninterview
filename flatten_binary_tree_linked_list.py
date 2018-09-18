

def flatten(root):
    """
        a
    b       c
    a
        b
            c
    """
    if not root:
        return

    flatten(root.left)
    flatten(root.right)

    right = root.right
    root.right = root.left
    root.left = None
    while root.right:
        root = root.right
    root.right = right
