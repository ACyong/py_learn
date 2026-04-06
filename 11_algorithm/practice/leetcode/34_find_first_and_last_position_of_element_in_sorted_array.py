from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        for i, v in enumerate(nums):
            if v != target:
                continue
            if start == -1:
                start, end = i, i
            else:
                end += 1
        return [start, end]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 10))
