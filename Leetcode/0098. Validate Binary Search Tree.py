# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], maxVal=2147483648, minVal=-2147483649) -> bool:
        if root == None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        if root.left != None:
            if root.left.val >= root.val or not self.isValidBST(root.left, maxVal=root.val, minVal=minVal):
                return False
        if root.right != None:
            if root.right.val <= root.val or not self.isValidBST(root.right, maxVal=maxVal, minVal=root.val):
                return False
        return True
