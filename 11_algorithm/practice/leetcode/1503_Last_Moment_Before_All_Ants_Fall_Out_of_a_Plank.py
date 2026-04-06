from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        lastMoment = 0 if not left else max(left)
        if right:
            lastMoment = max(lastMoment, max(n - ant for ant in right))
        return lastMoment
