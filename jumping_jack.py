

def max_step(n, k):
    """
    Given n steps, return max number of steps
    where you avoid k.
    At each step (i), you can jump i steps.
    """
    nums = [1]
    for i in range(2, n+1):
        nums.append(nums[-1] + 1)

    if k in nums:
        return nums[-1] - 1
    else:
        return nums[-1]
