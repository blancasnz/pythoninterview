
def is_present(root, val):
    if not root:
        return 0
    if root.value == val:
        return 1

    if root.value > val:
        return is_present(root.left, val)
    else:
        return is_present(root.right, val)
