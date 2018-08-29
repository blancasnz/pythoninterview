import heapq


def find_kth_largest1(nums, k):
    """
    O(nlogn)
    """
    return sorted(nums, reverse=True)[k-1]


def find_kth_largest2(nums, k):
    """
    O(nlogk)
    """
    h = []
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
    return heapq.heappop(h)
