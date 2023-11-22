# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.maxDepth = 0
        self.result = 0

        self.dfs(root, 0)

        return self.result

    def dfs(self, root, depth):
        if root == None:
            return

        if depth > self.maxDepth:
            self.maxDepth = depth
            self.result = root.val
        elif depth == self.maxDepth:
            self.result += root.val

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
