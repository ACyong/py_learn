from typing import List


class Solution:
    # 主函数，计算岛屿数量
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        # 遍历 grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # 每发现一个岛屿，岛屿数量加一
                    res += 1
                    # 然后使用 DFS 将岛屿淹了
                    self.dfs(grid, i, j)

        return res

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            # 超出索引边界
            return
        if grid[i][j] == '0':
            # 已经是海水了
            return
        # 将 (i, j) 变成海水
        grid[i][j] = '0'

        # 淹没上下左右边界
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
