
def expand(s, i):
    start = end = i
    while start > 0 and s[start-1] == s[i]:
        start -= 1
    while end < len(s) - 1 and s[end+1] == s[i]:
        end += 1

    while start > 0 and end < len(s) - 1 and s[start-1] == s[end+1]:
        start -= 1
        end += 1

    return start, end


def longest_palindrome(s):
    max_length = 0
    start = end = 0

    for i in range(len(s)):
        left, right = expand(s, i)
        if (right - left) > max_length:
            start = left
            end = right
            max_length = right - left
    return s[start:end+1]
