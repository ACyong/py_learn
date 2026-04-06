class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = left + ((right - left) >> 1)
            tmp = mid * mid
            if tmp < x:
                left = mid + 1
            elif tmp > x:
                right = mid - 1
            else:
                return mid
        return right
