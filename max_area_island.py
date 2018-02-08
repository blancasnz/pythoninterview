
class Solution(object):

    def max_area(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        visited = [
            [False for _ in range(len(grid[0]))]
            for _ in range(len(grid))
        ]

        def dfs(y, x):
            if not (0 <= y < len(grid)):
                return 0

            if not (0 <= x < len(grid[0])):
                return 0

            if visited[y][x]:
                return 0

            if grid[y][x] == 0:
                return 0

            visited[y][x] = True
            return 1 + dfs(y-1, x) + dfs(y+1, x) + dfs(y, x-1) + dfs(y, x+1)

        max_area = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                max_area = max(max_area, dfs(row, column))

        return max_area
