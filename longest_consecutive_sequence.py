

def longest_consecutive_seq(nums):

    s = set(nums)
    max_len = 0
    for i in range(len(nums)):
        current_len = 1
        seq = nums[i]
        if seq - 1 not in s:
            while seq + 1 in s:
                current_len += 1
                seq += 1
        max_len = max(max_len, current_len)

    return max_len
