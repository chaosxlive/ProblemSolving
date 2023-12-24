# https://leetcode.com/problems/recover-binary-search-tree/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x = y = predecessor = pred = None

        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root

                    predecessor.right = None
                    root = root.right
            else:
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root
                root = root.right

        x.val, y.val = y.val, x.val
