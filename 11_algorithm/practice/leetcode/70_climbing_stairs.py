class Solution:
    def climbStairs(self, n: int) -> int:
        i, j, f = 1, 2, 3
        if n == 1:
            return i
        if n == 2:
            return j
        if n == 3:
            return f
        while n > 3:
            i, j, f = j, f, j + f
            n -= 1
        return f

    def climbStairs1(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n+1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3

    def climbStairs2(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs2(n-2) + self.climbStairs2(n-1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(32))
    print(solution.climbStairs1(32))
    print(solution.climbStairs2(32))
