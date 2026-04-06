from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return right + 1

    def searchInsert1(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num >= target:
                return index
        return len(nums)

    def searchInsert2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] >= target:
                right = mid - 1
            else:
                if mid == (len(nums) - 1) or nums[mid + 1] >= target:
                    return mid + 1
                left = mid + 1
        return 0


if __name__ == '__main__':
    Solution().searchInsert2([1, 3, 5, 6], 7)
