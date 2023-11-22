# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.path = []
        self.pathP = None
        self.pathQ = None

        self.traverse(root)
        index = min(len(self.pathP), len(self.pathQ)) - 1
        while True:
            if self.pathP[index] == self.pathQ[index]:
                return self.pathP[index]
            index -= 1

    def traverse(self, root):
        self.path.append(root)
        if root == self.p:
            self.pathP = self.path[:]
        elif root == self.q:
            self.pathQ = self.path[:]

        if root.left != None:
            self.traverse(root.left)
        if root.right != None:
            self.traverse(root.right)

        self.path.pop()
