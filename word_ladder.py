

def word_ladder(start, end, words):

    output = []
    dfs(start, end, set(words), [start], output, set())
    if not output:
        return []

    shortest = []
    for path in sorted(output, key=len):
        if not shortest:
            shortest.append(path)
        elif len(path) == len(shortest[-1]):
            shortest.append(path)
    return shortest


def dfs(current, end, word_set, path, output, visited):
    if current in visited:
        return
    if current == end:
        output.append(path)
        return

    visited.add(current)

    for i in range(len(current)):
        letter_replacements = set([word[i] for word in word_set])
        for r in letter_replacements:
            new_word = current[:i] + r + current[i+1:]
            if new_word not in word_set:
                continue

            dfs(new_word, end, word_set, path +
                [new_word], output, visited)

    visited.discard(current)
