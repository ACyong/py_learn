from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0] * length
        diff = [0] * length
        for i in range(1, length):
            diff[i] = nums[i] - nums[i - 1]
        for update in updates:
            self._modify_nums(update, length, diff)
        return self._get_result(length, diff)

    @staticmethod
    def _modify_nums(update: List[int], length: int, diff: List[int]):
        diff[update[0]] += update[2]
        if update[1] + 1 < length:
            diff[update[1] + 1] -= update[2]

    @staticmethod
    def _get_result(length: int, diff: List[int]):
        res = [0] * length
        res[0] = diff[0]
        for i in range(1, length):
            res[i] = res[i - 1] + diff[i]
        return res


if __name__ == '__main__':
    print(Solution().getModifiedArray(length=5, updates=[[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
