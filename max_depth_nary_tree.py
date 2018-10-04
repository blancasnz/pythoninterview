

def max_depth(root):
    if not root:
        return 0

    max_height = 1
    for child in root.children:
        max_height = max(max_height, 1 + max_depth(child))
    return max_height
