class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_max_binary_tree(nums):
    if not nums:
        return None

    m = max(nums)
    index = nums.index(m)

    root = TreeNode(m)
    root.left = construct_max_binary_tree(nums[:index])
    root.right = construct_max_binary_tree(nums[index+1:])
    return root
