# 超时
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp(m - 1, n - 1)

    def dp(self, x, y):
        if x == 0 and y == 0:
            return 1
        if x < 0 or y < 0:
            return 0
        # 到达(x, y)的路径数等于到达(x - 1, y)和(x, y - 1)路径数之和
        return self.dp(x - 1, y) + self.dp(x, y - 1)


class Solution1:
    # 增加备忘录
    memo = None

    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[0 for _ in range(n)] for _ in range(m)]
        return self.dp(m - 1, n - 1)

    def dp(self, x, y):
        if x == 0 and y == 0:
            return 1
        if x < 0 or y < 0:
            return 0
        if self.memo[x][y] > 0:
            return self.memo[x][y]
        # 到达(x, y)的路径数等于到达(x - 1, y)和(x, y - 1)路径数之和
        self.memo[x][y] = self.dp(x - 1, y) + self.dp(x, y - 1)
        return self.memo[x][y]


# 迭代的方式
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # 增加备忘录
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePaths1(self, m: int, n: int) -> int:
        cur = [0 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[n - 1]
