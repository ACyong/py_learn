from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        # 遍历 grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 每发现一个岛屿，岛屿数量加一
                    res = max(res, self.dfs(grid, i, j))

        return res

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            # 超出索引边界
            return 0
        if grid[i][j] == 0:
            # 已经是海水了
            return 0
        # 将 (i, j) 变成海水
        grid[i][j] = 0

        # 淹没上下左右边界
        return self.dfs(grid, i + 1, j) + \
            self.dfs(grid, i, j + 1) + \
            self.dfs(grid, i - 1, j) + \
            self.dfs(grid, i, j - 1) + 1
