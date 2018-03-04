

class Solution(object):

    def min_bst(self, root):

        nodes = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)

        inorder(root)

        return min(nodes[i] - nodes[i-1] for i in range(1, len(nodes)))
