# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def findNode(root, nodeVal, path):
            path.append(root)
            if root == nodeVal:
                return True

            if root.left != None and findNode(root.left, nodeVal, path):
                return True
            if root.right != None and findNode(root.right, nodeVal, path):
                return True
            
            path.pop()
            return False

        pathP, pathQ = [], []
        findNode(root, p, pathP)
        findNode(root, q, pathQ)

        result = None
        index = 0
        while index < len(pathP) and index < len(pathQ):
            if pathP[index].val != pathQ[index].val:
                break
            result = pathP[index]
            index += 1
        return result
