from typing import List


class Solution42:
    # 超时
    def trap(self, height: List[int]) -> int:
        res, n = 0, len(height)
        for i in range(1, n - 1):
            r_max, l_max = 0, 0
            for j in range(i, n):
                r_max = max(r_max, height[j])
            for j in range(i, -1, -1):
                l_max = max(l_max, height[j])
            res = res + min(r_max, l_max) - height[i]
        return res

    # 优化: 增加备忘录
    def trap1(self, height: List[int]) -> int:
        res, n = 0, len(height)
        r_max, l_max = [0] * n, [0] * n
        l_max[0] = height[0]
        r_max[n - 1] = height[n - 1]
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])
        for i in range(1, n - 1):
            res += min(l_max[i], r_max[i]) - height[i]
        return res

    # 左右指针夹逼
    def trap2(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height) - 1
        l_max, r_max = 0, 0
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res


class Solution11:
    # 超时
    def maxArea(self, height: List[int]) -> int:
        res = 0
        # 两个指针不重复遍历列表
        for i in range(len(height)):
            for j in range(1, len(height)):
                res = max(res, (j - i) * min(height[i], height[j]))
        return res

    # 左右指针夹逼
    def maxArea1(self, height: List[int]) -> int:
        res, left, right = 0, 0, len(height) - 1
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    Solution42().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
