from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp, times = 0, 0
        for i in nums:
            if times == 0:
                temp = i
                times += 1
            else:
                if temp == i:
                    times += 1
                else:
                    times -= 1
        return temp
