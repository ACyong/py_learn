# 自顶向下递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib1(n):
    def helper(n, memo):
        if n == 1 or n == 2:
            return 1
        if memo[n] != 0:
            return memo[n]
        memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
        return memo[n]

    if n < 1:
        return 0
    memo = [0] * (n + 1)
    return helper(n, memo)


# 自底向上递推
def fib2(n):
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib3(n):
    if n == 1 or n == 2:
        return 1
    pre, cur = 1, 1
    for i in range(3, n + 1):
        count = pre + cur
        pre, cur = cur, count
    return cur


if __name__ == '__main__':
    print(fib(20))
    print(fib1(20))
    print(fib2(20))
    print(fib3(20))
