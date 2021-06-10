# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def checkSym(left, right):
            if left == None and right == None:
                return True
            elif left != None and right != None:
                if left.val != right.val:
                    return False
                return checkSym(left.left, right.right) and checkSym(left.right, right.left)
            return False

        return checkSym(root.left, root.right)
