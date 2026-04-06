from typing import List


def coin_change(coins: List[int], amount: int):
    def dp(n):
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1

        # 求最⼩值，所以初始化为正⽆穷
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            # ⼦问题⽆解，跳过
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        return res if res != float('INF') else -1

    return dp(amount)


def coin_change1(coins: List[int], amount: int):
    memo = dict()

    def dp(n):
        if n in memo:
            return memo[n]
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1

        # 求最⼩值，所以初始化为正⽆穷
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            # ⼦问题⽆解，跳过
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)


def coin_change2(coins: List[int], amount: int):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(0, amount + 1):
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return -1 if dp[amount] == amount + 1 else dp[amount]


if __name__ == '__main__':
    print(coin_change([1, 2, 5], 11))
    print(coin_change1([1, 2, 5], 11))
    print(coin_change2([1, 2, 5], 11))
