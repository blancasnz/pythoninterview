
def permute(nums):
    if len(nums) == 1:
        return [nums]

    if not nums:
        return [[]]

    output = []
    for i in range(len(nums)):
        prefix = nums[i]
        remaining = nums[0:i] + nums[i+1:]

        for perm in permute(remaining):
            perm.insert(0, prefix)
            output.append(perm)
    return output
