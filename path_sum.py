
def path_sum(root, target):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target

    return (
        path_sum(root.left, target-root.val) or
        path_sum(root.right, target-root.val)
    )
