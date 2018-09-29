
def work_break_ii(s, word_list):
    output = []
    find_words(s, set(word_list), [], output)
    return output


def find_words(s, word_set, path, output):
    if not s:
        output.append(' '.join(path))

    for i in range(len(s) + 1):
        prefix = s[:i]
        suffix = s[i:]
        if prefix in word_set:
            find_words(suffix, word_set, path + [prefix], output)


def memo_word_break_ii(s, word_list):
    return find_words_memo(s, set(word_list), {})


def find_words_memo(s, word_set, memo):
    if not s:
        return []
    if s in memo:
        return memo[s]

    output = []
    for word in word_set:
        if not s.startswith(word):
            continue
        if len(s) == len(word):
            output.append(s)
        else:
            suffix = s[len(word):]
            others = find_words_memo(suffix, word_set, memo)
            for w in others:
                output.append(word + ' ' + w)

    memo[s] = output
    return memo[s]
