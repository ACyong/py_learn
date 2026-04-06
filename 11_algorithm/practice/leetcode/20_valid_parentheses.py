# -*- coding: utf-8 -*-


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pare_map = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in pare_map:
                stack.append(c)
            elif not stack or pare_map[c] != stack.pop():
                return False
        return not stack
