from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self._generate(result, left=0, right=0, n=n, s="")
        return result

    def _generate(self, result, left, right, n, s):
        if left == n and right == n:
            result.append(s)
            return
        if left < n:
            self._generate(result, left + 1, right, n, s + "(")
        if left > right:
            self._generate(result, left, right + 1, n, s + ")")


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
