# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self.dfs(root, low, high)

    def dfs(self, root: TreeNode, low: int, high: int):
        if root == None:
            return 0

        ret = 0
        if low <= root.val <= high:
            ret = root.val
        if low <= root.val:
            ret += self.dfs(root.left, low, high)
        if high >= root.val:
            ret += self.dfs(root.right, low, high)
        
        return ret
        