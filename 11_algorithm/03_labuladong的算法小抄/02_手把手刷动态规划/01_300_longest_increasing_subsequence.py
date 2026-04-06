from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        dp = []
        for i in range(0, len(nums)):
            dp.append(1)
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLTS2(self, nums: List[int]) -> int:
        top = [0 for _ in range(len(nums))]
        piles = 0
        for num in nums:
            left, right = 0, piles
            while left < right:
                mid = left + (right - left) // 2
                if top[mid] == num:
                    right = mid
                elif top[mid] < num:
                    left = mid + 1
                elif top[mid] > num:
                    right = mid
            if left == piles:
                piles += 1
            top[left] = num
        return piles
