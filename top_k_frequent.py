from collections import Counter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    sorted_by_occur = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return [pair[0] for pair in sorted_by_occur[:k]]
