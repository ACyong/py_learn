class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(memo, stairs):
            if stairs in memo:
                return memo[stairs]
            if stairs <= 2:
                return stairs
            memo[stairs] = dp(memo, stairs-1) + dp(memo, stairs - 2)
            return memo[stairs]

        memo = {}
        return dp(memo, n)

    def climbStairs1(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n + 1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3
