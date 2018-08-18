
def inorder_traversal(root):
    if not root:
        return []

    output = inorder_traversal(root.left)
    output.root.val
    output.extend(inorder_traversal(root.right))
    return output


def inorder_iterative(root):
    output = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        item = stack.pop()
        output.append(item.val)
        current = item.right

    return output
