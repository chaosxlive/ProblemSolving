# https://leetcode.com/problems/same-tree/

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p is None and q is None:
            return True

        return self.travel(p, q)

    def travel(self, p, q):
        if p.val != q.val:
            return False

        if (p.left is None and q.left is not None) or (p.left is not None and q.left is None) or (p.right is None and q.right is not None) or (p.right is not None and q.right is None):
            return False
        if p.left is not None and not self.travel(p.left, q.left):
            return False
        if p.right is not None and not self.travel(p.right, q.right):
            return False
        return True
