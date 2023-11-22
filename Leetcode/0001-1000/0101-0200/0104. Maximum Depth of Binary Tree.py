# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        result = 0
        result = max(self.maxDepth(root.left), result)
        result = max(self.maxDepth(root.right), result)
            
        return result + 1

