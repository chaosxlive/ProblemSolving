# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.preorder = preorder
        self.inorder = inorder
        self.indexPreorder = 0

        return self.getSubTree(0, len(self.preorder))

    def getSubTree(self, left, right):
        if left >= right:
            return None
        index = left
        while self.inorder[index] != self.preorder[self.indexPreorder]:
            index += 1
        self.indexPreorder += 1
        leftNode = self.getSubTree(left, index)
        rightNode = self.getSubTree(index + 1, right)
        return TreeNode(self.inorder[index], leftNode, rightNode)
