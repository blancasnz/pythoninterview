
def max_sub_array(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]

    max_sum = 0
    for i in range(i, len(nums)):
        add = dp[i-1] if dp[i-1] > 0 else 0
        dp[i] = nums[i] + add
        max_sum = max(max_sum, dp[i])

    return max_sum
