# https://leetcode.com/problems/maximum-average-subtree/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.result = 0.0

        def dfs(node):
            val, cnt = node.val, 1
            if node.left is not None:
                leftVal, leftCnt = dfs(node.left)
                val += leftVal
                cnt += leftCnt
            if node.right is not None:
                rightVal, rightCnt = dfs(node.right)
                val += rightVal
                cnt += rightCnt
            self.result = max(self.result, val / cnt)
            return val, cnt

        dfs(root)

        return self.result
