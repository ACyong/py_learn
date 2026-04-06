class Solution:
    def dp(self, stairs, memo):
        if stairs in memo:
            return memo[stairs]
        if stairs <= 2:
            return stairs
        memo[stairs] = self.dp(stairs - 1, memo) + self.dp(stairs - 2, memo)
        return memo[stairs]

    def climbStairs(self, n: int) -> int:
        res = {}
        return self.dp(n, res)
