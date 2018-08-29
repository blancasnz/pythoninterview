

def dfs(nums, index, path, output):
    output.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i + 1, path + [nums[i]], output)


def subset(nums):
    output = []
    dfs(nums, 0, [], output)
    return output
