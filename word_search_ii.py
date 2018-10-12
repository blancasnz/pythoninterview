
def find_words(board, words):
    output = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            current_search = []
            visited = set()
            dfs(board, set(words), i, j, '', current_search, visited)
            output.extend(current_search)

    return output


def dfs(board, word_set, y, x, current_str, output, visited):
    if (y, x) in visited:
        return
    if not (0 <= y <= len(board) - 1):
        return
    if not (0 <= x <= len(board[0]) - 1):
        return

    visited.add((y, x))
    current_str = current_str + board[y][x]

    for word in word_set:
        if current_str == word:
            output.append(word)

        if word.startswith(current_str):
            dfs(board, word_set, y+1, x, current_str, output, visited)
            dfs(board, word_set, y, x+1, current_str, output, visited)
            dfs(board, word_set, y-1, x, current_str, output, visited)
            dfs(board, word_set, y, x-1, current_str, output, visited)

        visited.discard((y, x))
