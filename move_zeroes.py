
def move_zeroes(nums):
    for i in range(len(nums)):
        if nums[i] != 0:
            continue

        for j in range(i, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                break
