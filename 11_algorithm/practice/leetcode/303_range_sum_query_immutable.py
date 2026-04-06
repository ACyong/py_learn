from typing import List


# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     def sumRange(self, left: int, right: int) -> int:
#         res = 0
#         for i in range(left, right+1):
#             res += self.nums[i]
#         return res


class NumArray:

    def __init__(self, nums: List[int]):
        length = len(nums) + 1
        self.pre_nums = [0] * length
        for i in range(1, length):
            self.pre_nums[i] = self.pre_nums[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_nums[right + 1] - self.pre_nums[left]
