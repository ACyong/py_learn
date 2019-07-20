# -*- coding: utf-8 -*-


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s_dict, t_dict = {}, {}
    #
    #     for item in s:
    #         s_dict[item] = s_dict.get(item, 0) + 1
    #
    #     for item in t:
    #         t_dict[item] = t_dict.get(item, 0) + 1
    #
    #     return s_dict == t_dict

    def isAnagram(self, s: str, t: str) -> bool:
        s_list, t_list = [0] * 26, [0] * 26

        for item in s:
            s_list[ord(item) - ord('a')] += 1

        for item in t:
            t_list[ord(item) - ord('a')] += 1

        return s_list == t_list


if __name__ == '__main__':
    print(Solution().isAnagram('rat', 'rat'))
