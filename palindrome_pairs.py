

def is_palindrome(word):
    return word == word[::-1]


def palindrome_pairs_brute(words):
    output = []
    for i in range(len(words)):
        for j in range(i, len(words)):
            if is_palindrome(words[i]+words[j]):
                output.append([i, j])
            if is_palindrome(words[j]+words[i]):
                output.append([j, i])
    return output


def palindrome_pairs(words):
    w = {word: i for i, word in enumerate(words)}

    output = []
    for j in range(len(words)):
        word = words[j]
        for i in range(len(word)+1):
            prefix = word[:i]
            suffix = word[i:]

            if prefix == prefix[::-1]:
                reversed_suffix = suffix[::-1]
                if reversed_suffix in w and w[reversed_suffix] != j:
                    output.append([w[reversed_suffix], j])

            if suffix == suffix[::-1]:
                reversed_prefix = prefix[::-1]
                if reversed_prefix in w and w[reversed_prefix] != j:
                    output.append([j, w[reversed_prefix]])

    return output
