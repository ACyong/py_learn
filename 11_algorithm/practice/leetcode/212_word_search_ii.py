import collections
from typing import List


class Solution:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    END_OF_WORD = "#"

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.result = set()
        trie = self.init_trie(words)
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in trie:
                    self.dfs(board, i, j, "", trie)
        return list(self.result)

    def init_trie(self, words):
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[self.END_OF_WORD] = self.END_OF_WORD
        return root

    def dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if self.END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        tmp, board[i][j] = board[i][j], "@"
        # 四联通图遍历
        for k in range(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != "@" \
                    and board[x][y] in cur_dict:
                self.dfs(board, i, j, cur_word, cur_dict)
        board[i][j] = tmp
