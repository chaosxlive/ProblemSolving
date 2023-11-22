# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.result = 0

        def dfs(node: TreeNode):
            total = node.val
            cnt = 1
            if node.left is not None:
                totalLeft, cntLeft = dfs(node.left)
                total += totalLeft
                cnt += cntLeft
            if node.right is not None:
                totalRight, cntRight = dfs(node.right)
                total += totalRight
                cnt += cntRight
            if total // cnt == node.val:
                self.result += 1
            return total, cnt

        dfs(root)
        return self.result
