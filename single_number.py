def single_number(nums):
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    for num, count in counts.items():
        if count == 1:
            return num

    return -1
