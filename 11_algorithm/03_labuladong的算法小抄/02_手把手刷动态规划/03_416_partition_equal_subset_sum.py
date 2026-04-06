from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False

        n = len(nums)
        nums_sum //= 2
        dp = [[False for _ in range(nums_sum + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, nums_sum + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][nums_sum]

    def canPartition1(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False

        n = len(nums)
        nums_sum //= 2
        dp = [False for _ in range(nums_sum + 1)]
        dp[0] = True
        for i in range(n):
            for j in range(nums_sum, 0, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]

        return dp[nums_sum]


if __name__ == '__main__':
    print(Solution().canPartition([1, 5, 11, 5]))
    print(Solution().canPartition1([1, 5, 11, 5]))
