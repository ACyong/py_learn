from typing import List


# Definition for a binary 05_tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level_helper(root, res, 0)
        return res

    def level_helper(self, root: TreeNode, res: List[List[int]], level: int) -> None:
        if root is None:
            return
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.level_helper(root.left, res, level+1)
        self.level_helper(root.right, res, level+1)
