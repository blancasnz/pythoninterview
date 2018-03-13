from collections import Counter


def one_away(input1, input2):
    counts = {}
    for char in input1.lower():
        counts[char] = counts.get(char, 0) + 1

    for char in input2.lower():
        counts[char] = counts.get(char, 0) - 1
        if counts[char] == 0:
            counts.pop(char)

    return len(counts) <= 2


def one_away_v2(input1, input2):
    count1 = Counter(input1.lower())
    count2 = Counter(input2.lower())
    count1.subtract(count2)
    filtered = {k: v for k, v in count1.items() if v != 0}
    return len(filtered) <= 2
