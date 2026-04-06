from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index, num in enumerate(nums):
            nums[index] = num * num
        nums.sort()
        return nums

    def sortedSquares1(self, nums: List[int]) -> List[int]:
        start, index, end = 0, len(nums) - 1, len(nums) - 1
        result = [-1] * (index + 1)
        while start <= end:
            start_res = nums[start] * nums[start]
            end_res = nums[end] * nums[end]
            if start_res > end_res:
                result[index] = start_res
                start += 1
            else:
                result[index] = end_res
                end -= 1
            index -= 1
        return result


if __name__ == '__main__':
    Solution().sortedSquares1([-4, -1, 0, 3, 10])
