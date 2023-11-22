# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            maxResult = root.val
            leftResult = leftPathSum = rightResult = rightPathSum = 0
            if root.left is not None:
                leftResult, leftPathSum = dfs(root.left)
                maxResult = max(maxResult, leftResult, leftPathSum + root.val)
            if root.right is not None:
                rightResult, rightPathSum = dfs(root.right)
                maxResult = max(maxResult, rightResult, rightPathSum + root.val)
            if root.left is not None and root.right is not None:
                maxResult = max(maxResult, leftPathSum + root.val + rightPathSum)
            maxPathSum = max(root.val, leftPathSum + root.val, rightPathSum + root.val)
            return maxResult, maxPathSum

        return dfs(root)[0]
