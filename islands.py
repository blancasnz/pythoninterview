from collections import deque


def count_islands(grid):
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]

    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not visited[i][j] and grid[i][j] == 1:
                explore(grid, visited, i, j)
                island_count += 1
    return island_count


def explore(grid, visited, i, j):
    q = deque()
    q.append((i, j))

    while q:
        y, x = q.popleft()
        visited[y][x] = True

        for dy, dx in zip([0, 0, 1, -1], [-1, 1, 0, 0]):
            if (
                0 <= y + dy <= len(grid) - 1 and
                0 <= x + dx <= len(grid[0]) - 1 and
                not visited[y + dy][x + dx] and
                grid[y + dy][x + dx] == 1
            ):
                q.append((y + dy, x + dx))
