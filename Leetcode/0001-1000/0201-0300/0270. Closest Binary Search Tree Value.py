# https://leetcode.com/problems/closest-binary-search-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result = root.val
        diff = abs(target - root.val)
        if root.left is not None:
            l = self.closestValue(root.left, target)
            diffL = abs(target - l)
            if diffL < diff:
                result = l
        if root.right is not None:
            l = self.closestValue(root.right, target)
            diffL = abs(target - l)
            if diffL < diff:
                result = l
        return result
