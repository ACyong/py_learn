from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        diff = [0] * n
        for i in range(1, n):
            diff[i] = nums[i] - nums[i - 1]
        for booking in bookings:
            self._modify_nums(booking, n, diff)
        return self._get_result(n, diff)

    @staticmethod
    def _modify_nums(booking: List[int], n: int, diff: List[int]):
        diff[booking[0] - 1] += booking[2]
        if booking[1] < n:
            diff[booking[1]] -= booking[2]

    @staticmethod
    def _get_result(n: int, diff: List[int]):
        res = [0] * n
        res[0] = diff[0]
        for i in range(1, n):
            res[i] = res[i - 1] + diff[i]
        return res


if __name__ == '__main__':
    print(Solution().corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
