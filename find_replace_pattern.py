

def find_replace_pattern(words, pattern):
    output = []
    for word in words:
        if is_match(word, pattern):
            output.append(word)
    return output


def is_match(word, pattern):
    if len(word) != len(pattern):
        return False

    word_pattern = {}
    pattern_word = {}
    for a, b in zip(word, pattern):
        if a not in word_pattern and b not in pattern_word:
            word_pattern[a] = b
            pattern_word[b] = a
        elif word_pattern.get(a) != b or pattern_word.get(b) != a:
            return False

    return True
