class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False

    def isAnagram1(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}
        for c in s:
            count_s.setdefault(c, 0)
            count_s[c] += 1
        for c in t:
            count_t.setdefault(c, 0)
            count_t[c] += 1

        if count_s == count_t:
            return True
        return False

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for i in range(len(s)):
            counts.setdefault(s[i], 0)
            counts[s[i]] += 1
            counts[t[i]] -= 1
        for _, val in counts.items():
            if val != 0:
                return False
        return True
