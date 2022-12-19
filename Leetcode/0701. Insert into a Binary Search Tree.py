# https://leetcode.com/problems/insert-into-a-binary-search-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            newNode = TreeNode(val)
            return newNode
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
                return root
            self.insertIntoBST(root.left, val)
            return root
        if root.right is None:
            root.right = TreeNode(val)
            return root
        self.insertIntoBST(root.right, val)
        return root
