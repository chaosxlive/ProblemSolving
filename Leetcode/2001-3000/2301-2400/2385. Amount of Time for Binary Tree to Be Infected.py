# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.result = 0

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0

            depthLeft, depthRight = dfs(node.left), dfs(node.right)
            if node.val == start:
                self.result = max(depthLeft, depthRight)
                return -1
            if depthLeft >= 0 and depthRight >= 0:
                return max(depthLeft, depthRight) + 1
            self.result = max(self.result, abs(depthLeft) + abs(depthRight))
            return min(depthLeft, depthRight) - 1

        dfs(root)
        return self.result
