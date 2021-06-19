# https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.result = 0
        self.traversal(root)
        return self.result

    def traversal(self, root):
        if root == None:
            return 0
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        self.result += abs(left - right)
        return root.val + left + right
