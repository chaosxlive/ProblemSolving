# https://leetcode.com/problems/sum-of-left-leaves/

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def traversal(root, isLeft):
            if root.left == None and root.right == None:
                if isLeft:
                    return root.val
                return 0

            result = 0
            if root.left != None:
                result += traversal(root.left, True)
            if root.right != None:
                result += traversal(root.right, False)
            return result

        return traversal(root, False)
