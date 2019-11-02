# -*- coding: utf-8 -*-

class Solution:
    def singleNumber(self, nums):
        d = {}
        for n in nums:
            if n in d:
                del d[n]
            else: 
                d[n] = 1
        return list(d)

    def singleNumber_2(self, nums):
        from collections import Counter
        # elect two least freq element
        freq = Counter(nums).most_common()[-2:]
        # pick the element not the frequence 
        return [x[0] for x in freq]


a = Solution().singleNumber([1,2,1,3,2,5])
print(a)
