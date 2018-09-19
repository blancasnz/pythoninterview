

def dfs(mat, y, x, dp):
    if dp[y][x]:
        return dp[y][x]

    max_len = 0
    current_num = mat[y][x]
    if y > 0 and mat[y-1][x] > current_num:
        max_len = max(max_len, dfs(mat, y-1, x, dp))
    if y < len(mat) - 1 and mat[y+1][x] > current_num:
        max_len = max(max_len, dfs(mat, y+1, x, dp))
    if x > 0 and mat[y][x-1] > current_num:
        max_len = max(max_len, dfs(mat, y, x-1, dp))
    if x < len(mat[0]) - 1 and mat[y][x+1] > current_num:
        max_len = max(max_len, dfs(mat, y, x+1, dp))

    dp[y][x] = 1 + max_len
    return dp[y][x]


def longest_increasing_sequence(matrix):
    dp = [[0 for _ in range(matrix[0])] for _ in range(len(matrix))]
    max_len = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_len = max(max_len, dfs(matrix, i, j, dp))
    return max_len
