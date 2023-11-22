# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(root):
            if root == None:
                return (0, True)
            leftCount, leftBalanced = dfs(root.left)
            rightCount, rightBalanced = dfs(root.right)
            if not leftBalanced or not rightBalanced:
                return (0, False)
            if abs(leftCount - rightCount) > 1:
                return (0, False)
            return (max(leftCount, rightCount) + 1, True)

        return dfs(root)[1]
