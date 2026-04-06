from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, left, right, s = [], 0, 0, ""
        self.dp(res, n, left, right, s)
        return res

    def dp(self, res, n, left, right, s):
        if left == n and right == n:
            res.append(s)
            return
        if left < n:
            self.dp(res, n, left + 1, right, s + "(")
        if right < left:
            self.dp(res, n, left, right + 1, s + ")")
