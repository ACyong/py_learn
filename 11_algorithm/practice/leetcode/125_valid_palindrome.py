class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        target_s = ""
        for char in lower_s:
            if char in "abcdefghijklmnopqrstuvwxyz0123456789":
                target_s += char
        return target_s == target_s[::-1]

    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


if __name__ == '__main__':
    # 3
    solution = Solution()
    print(solution.isPalindrome(s="dhfa"))

    print(solution.isPalindrome1(s="ddddd"))
