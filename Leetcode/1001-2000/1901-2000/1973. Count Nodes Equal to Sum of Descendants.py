# https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def equalToDescendants(self, root: Optional[TreeNode]) -> int:

        self.result = 0

        def dfs(node):
            childSum = 0
            if node.left is not None:
                childSum += dfs(node.left)
            if node.right is not None:
                childSum += dfs(node.right)
            if node.val == childSum:
                self.result += 1
            return node.val + childSum

        dfs(root)
        return self.result
