
def partition_labels(s):
    output = []
    last = {char: index for index, char in enumerate(s)}
    start = 0
    current_max = 0
    for index, char in enumerate(s):
        current_max = max(current_max, last[char])
        if current_max == index:
            output.append(current_max - start + 1)
            start = index + 1
    return output
