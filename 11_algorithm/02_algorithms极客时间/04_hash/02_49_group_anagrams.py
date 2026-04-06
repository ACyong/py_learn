import collections
from typing import List


class Solution:
    # 特征值归类, 一般采用hash表来存储
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())
