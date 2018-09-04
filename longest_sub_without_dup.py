

def length_of_longest_sub(input):
    left = 0
    right = 0
    max_sub = 0

    chars = set()
    while right < len(input):
        if input[right] not in chars:
            chars.add(input[right])
            max_sub = max(max_sub, len(chars))
            right += 1
        else:
            chars.discard(input[left])
            left += 1
    return max_sub
