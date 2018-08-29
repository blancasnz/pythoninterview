

def unique_paths(m, n):
    grid = [[0 for _ in range(n)] for _ in m]
    for i in n:
        grid[0][i] = 1
    for i in m:
        grid[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[m-1][n-1]
