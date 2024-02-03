# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.pathCounter = [0] * 10
        self.result = 0

        def dfs(node: TreeNode):
            self.pathCounter[node.val] += 1
            if node.left is None and node.right is None:
                oddCnt = 0
                for c in self.pathCounter:
                    if c & 1:
                        oddCnt += 1
                if oddCnt <= 1:
                    self.result += 1
            else:
                if node.left is not None:
                    dfs(node.left)
                if node.right is not None:
                    dfs(node.right)

            self.pathCounter[node.val] -= 1

        dfs(root)

        return self.result
