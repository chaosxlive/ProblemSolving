# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left != None:
            if root.val != root.left.val or not self.isUnivalTree(root.left):
                return False
        if root.right != None:
            if root.val != root.right.val or not self.isUnivalTree(root.right):
                return False
        return True
