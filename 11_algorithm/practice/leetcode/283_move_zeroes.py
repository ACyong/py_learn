from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_position = 0
        set_zero_position = False
        length = len(nums)
        for item in range(length):
            if nums[item] != 0:
                if not set_zero_position:
                    continue
                nums[zero_position] = nums[item]
                nums[item] = 0
                zero_position += 1
            if not set_zero_position:
                zero_position = item
                set_zero_position = True

    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_position = 0
        length = len(nums)
        for item in range(length):
            if nums[item] != 0:
                nums[zero_position] = nums[item]
                if item != zero_position:
                    nums[item] = 0
                zero_position += 1

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for item in nums:
            if item == 0:
                nums.append(0)
                nums.remove(0)

    def moveZeroes3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_position = 0
        length = len(nums)
        for item in range(length):
            if nums[item] != 0:
                nums[item], nums[zero_position] = nums[zero_position], nums[item]
                zero_position += 1

    def moveZeroes4(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[zero_count] = nums[i]
                zero_count += 1
        for j in range(zero_count, length):
            nums[j] = 0


if __name__ == '__main__':
    # 3
    L = [9, 0, 1, 0, 0, 4, 0, 0, 0, 5, 6, 0, 0, 0]
    print(L)
    solution = Solution()
    solution.moveZeroes(L)
    print(L)
    L = [9, 0, 1, 0, 0, 4, 0, 0, 0, 5, 6, 0, 0, 0]
    solution.moveZeroes1(L)
    print(L)
    L = [9, 0, 1, 0, 0, 4, 0, 0, 0, 5, 6, 0, 0, 0]
    solution.moveZeroes2(L)
    print(L)
    L = [9, 0, 1, 0, 0, 4, 0, 0, 0, 5, 6, 0, 0, 0]
    solution.moveZeroes3(L)
    print(L)
    L = [9, 0, 1, 0, 0, 4, 0, 0, 0, 5, 6, 0, 0, 0]
    solution.moveZeroes4(L)
    print(L)
