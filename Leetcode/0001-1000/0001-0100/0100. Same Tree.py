# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p == None and q == None:
            return True

        return self.travel(p, q)

    def travel(self, p, q):
        if p.val != q.val:
            return False

        if (p.left == None and q.left != None) or (p.left != None and q.left == None) or (p.right == None and q.right != None) or (p.right != None and q.right == None):
            return False
        if p.left != None and not self.travel(p.left, q.left):
            return False

        if p.right != None and not self.travel(p.right, q.right):
            return False
        return True
