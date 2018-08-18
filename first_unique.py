from collections import Counter


def first_unique(input):
    counts = Counter(input)
    for index, char in enumerate(input):
        if counts[char] == 1:
            return index
    return -1
