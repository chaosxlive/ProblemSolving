# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.result = 0

        return max(self.dfs(root), self.result)

    def dfs(self, root):
        l = self.dfs(root.left) + 1 if root.left else 0
        r = self.dfs(root.right) + 1 if root.right else 0
        self.result = max(self.result, l + r)
        return max(l, r)
