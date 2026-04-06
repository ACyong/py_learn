# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        return left_depth + right_depth + 1 \
            if left_depth == 0 or right_depth == 0 \
            else min(left_depth, right_depth) + 1
