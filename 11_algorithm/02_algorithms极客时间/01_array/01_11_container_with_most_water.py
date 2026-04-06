from typing import List


class Solution:
    # 超时
    def maxArea(self, height: List[int]) -> int:
        area = 0
        # 两个指针不重复遍历列表
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = max(area, (j - i) * min(height[i], height[j]))
        return area

    def maxArea1(self, height: List[int]) -> int:
        area = 0
        # 左右指针夹逼
        head, tail = 0, len(height) - 1
        while head < tail:
            area = max(area, (tail - head) * min(height[head], height[tail]))
            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1
        return area
