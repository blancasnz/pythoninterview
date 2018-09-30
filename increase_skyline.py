

def max_increase(grid):

    row_max = []
    col_max = []
    for i in range(len(grid)):
        row_max.append(max(grid[i]))
        col_max.append(max([row[i] for row in grid]))

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total += min(row_max[i], col_max[j]) - grid[i][j]
    return total
