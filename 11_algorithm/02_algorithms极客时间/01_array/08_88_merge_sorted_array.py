from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sorted_nums = []
        p1, p2 = 0, 0

        while p1 < m or p2 < n:
            if p1 == m:
                sorted_nums.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted_nums.append((nums1[p1]))
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted_nums.append(nums1[p1])
                p1 += 1
            else:
                sorted_nums.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted_nums

    # 头号玩家：所有玩家都全力向前冲刺, 却不知道向后才是胜利之门。
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
