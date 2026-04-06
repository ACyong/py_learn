# Definition for a binary 05_tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.pre_order(root, res)
        return res

    def pre_order(self, root: Optional[TreeNode], res: List):
        if root is None:
            return
        res.append(root.val)
        self.pre_order(root.left, res)
        self.pre_order(root.right, res)
