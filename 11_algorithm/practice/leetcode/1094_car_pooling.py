from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for trip in trips:
            self._modify_nums(trip, diff)
        return self._get_result(diff, capacity)

    @staticmethod
    def _modify_nums(trip: List[int], diff: List[int]):
        diff[trip[1]] += trip[0]
        if trip[2] < len(diff):
            diff[trip[2]] -= trip[0]

    @staticmethod
    def _get_result(diff: List[int], capacity: int):
        res = [0] * 1001
        res[0] = diff[0]
        for i in range(1, 1001):
            res[i] = res[i - 1] + diff[i]
            if capacity < res[i-1]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().carPooling(trips=[[9,0,1],[3,3,7]], capacity=4))
