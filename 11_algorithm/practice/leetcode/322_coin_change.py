from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1

            res = float("INF")
            for coin in coins:
                sub_problem = dp(n - coin)
                if sub_problem == -1:
                    continue
                res = min(res, sub_problem + 1)
            memo[n] = res if res != float("INF") else -1
            return memo[n]

        return dp(amount)

    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(0, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == amount + 1 else dp[amount]
