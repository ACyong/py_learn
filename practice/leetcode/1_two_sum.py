class Solution:
    def twoSum(self, nums, target):
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