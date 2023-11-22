# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode], maxVal: int, minVal: int) -> int:
            result = 0
            maxVal = max(maxVal, root.val)
            minVal = min(minVal, root.val)
            if root.left is None and root.right is None:
                result = maxVal - minVal
            else:
                if root.left is not None:
                    result = max(result, dfs(root.left, maxVal, minVal))
                if root.right is not None:
                    result = max(result, dfs(root.right, maxVal, minVal))
            return result

        return dfs(root, root.val, root.val)
