from typing import List


class Solution1:
    """
    将two sum 问题就改为: nums 中可能有多对儿元素之和都等于 target，
    请你的算法返回所有和为 target 的元素对儿，其中不能出现重复
    """

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lo, hi = 0, len(nums) - 1
        res = []
        while lo < hi:
            sum_num = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if sum_num < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif sum_num > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res


class Solution15:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break  # 1. because of nums[j] > nums[i] > nums[k].
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j:  # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res


class Solution18:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets

        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets


if __name__ == '__main__':
    print(Solution1().twoSum([2, 7, 11, 15, 2, 7, 1, 8, 1, 8], 9))
