def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    visited = [[None] * len(grid[0]) for i in range(len(grid))]

    def dfs(y, x):
        if y == len(grid) - 1 and x == len(grid[0]) - 1:
            return grid[y][x]

        if visited[y][x]:
            return visited[y][x]

        down = float('inf')
        right = float('inf')
        if x != len(grid[0]) - 1:
            right = dfs(y, x + 1)
        if y != len(grid) - 1:
            down = dfs(y + 1, x)

        m = min(right, down) + grid[y][x]
        visited[y][x] = m
        return m

    return dfs(0, 0)
