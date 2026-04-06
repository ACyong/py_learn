from typing import List


class Solution:
    # 两个指针不重复遍历列表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_i in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num_i + nums[j] == target:
                    return [i, j]

    # 优化: 增加备忘录
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i, num in enumerate(nums):
            if target - num in result:
                return [result[target - num], i]
            result[num] = i

