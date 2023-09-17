# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node: TreeNode, isPrevLeft: bool, step: int):
            self.result = max(self.result, step)

            if node.left is not None:
                dfs(node.left, True, 1 if isPrevLeft else step + 1)
            if node.right is not None:
                dfs(node.right, False, step + 1 if isPrevLeft else 1)

        dfs(root, True, 0)
        dfs(root, False, 0)

        return self.result
