from typing import List


def backpack(n: int, w: int, wts: List[int], vals: List[int]) -> int:
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            # 不放入背包
            if j - wts[i-1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - wts[i - 1]] + vals[i - 1], dp[i - 1][j])
    return dp[n][w]


if __name__ == '__main__':
    print(backpack(3, 4, [2, 1, 3], [4, 2, 3]))
