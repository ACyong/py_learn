from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                curr_width = i - left - 1
                curr_height = min(height[left], height[i]) - height[top]
                ans += curr_width * curr_height
            stack.append(i)

        return ans
