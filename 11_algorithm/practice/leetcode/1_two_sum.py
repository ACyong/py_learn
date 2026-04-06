# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        for index, num in enumerate(nums):
            tmp = target - num
            if tmp in result:
                return [result[tmp], index]
            result[num] = index
        return []

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    solution = Solution()
    print(solution.twoSum(nums, 9))
    print(solution.twoSum1(nums, 9))
