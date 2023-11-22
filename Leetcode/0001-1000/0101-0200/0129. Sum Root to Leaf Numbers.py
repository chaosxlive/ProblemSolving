# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    result = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, current):
        if root is None:
            return
        val = current * 10 + root.val
        if root.left == None and root.right == None:
            self.result += val
        if root.left:
            self.dfs(root.left, val)
        if root.right:
            self.dfs(root.right, val)
