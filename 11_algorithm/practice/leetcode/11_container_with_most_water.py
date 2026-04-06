from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        max_area = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area

    def maxArea1(self, height: List[int]) -> int:
        length = len(height)
        i = 0
        j = length - 1
        max_area = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height))
    print(solution.maxArea1(height))
