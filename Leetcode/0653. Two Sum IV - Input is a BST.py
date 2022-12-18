# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return False
            if k - root.val in seen:
                return True
            seen.add(root.val)
            return dfs(root.left) or dfs(root.right)

        return dfs(root)
