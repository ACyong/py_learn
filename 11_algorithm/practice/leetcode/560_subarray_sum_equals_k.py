from typing import List


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         length = len(nums) + 1
#         pre_nums = [0] * length
#         for i in range(1, length):
#             pre_nums[i] = pre_nums[i-1] + nums[i-1]
#         res = 0
#         for i in range(1, length):
#             for j in range(i):
#                 if (pre_nums[i] - pre_nums[j]) != k:
#                     continue
#                 res += 1
#         return res


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         res, length = 0, len(nums)
#         for i in range(0, length):
#             sum_ = 0
#             for j in range(i, length):
#                 sum_ += nums[j]
#                 if sum_ == k:
#                     res += 1
#         return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_dict = {0: 1}
        res, sum_i = 0, 0
        for num in nums:
            sum_i += num
            sum_j = sum_i - k
            if sum_j in pre_dict:
                res += pre_dict[sum_j]
            pre_dict[sum_i] = pre_dict.setdefault(sum_i, 0) + 1
        return res


if __name__ == '__main__':
    print(Solution().subarraySum([1, 1, 1], 2))
