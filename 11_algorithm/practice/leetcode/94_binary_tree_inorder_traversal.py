# Definition for a binary 05_tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.in_order(root, res)
        return res

    def in_order(self, root: Optional[TreeNode], res: List) -> None:
        if root is None:
            return
        self.in_order(root.left, res)
        res.append(root.val)
        self.in_order(root.right, res)
