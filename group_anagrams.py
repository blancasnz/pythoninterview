from collections import defaultdict


def group_anagrams(strs):
    buckets = defaultdict(list)
    for s in strs:
        buckets[tuple(sorted(s))].append(s)
    return buckets.values()
