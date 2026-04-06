from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[low] = nums[fast]
                low += 1
            fast += 1
        return low
