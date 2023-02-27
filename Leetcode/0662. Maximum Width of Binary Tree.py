# https://leetcode.com/problems/maximum-width-of-binary-tree/

from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.lefts = defaultdict(lambda: float('inf'))
        self.rights = defaultdict(lambda: -1)
        self.maxRank = -1
        self.dfs(root, 0, 0)
        return max((self.rights[r] - self.lefts[r] + 1) for r in range(self.maxRank + 1))

    def dfs(self, root: TreeNode, pos: int, rank: int):
        self.lefts[rank] = min(self.lefts[rank], pos)
        self.rights[rank] = max(self.rights[rank], pos)
        self.maxRank = max(self.maxRank, rank)
        if root.left is not None:
            self.dfs(root.left, 2 * pos, rank + 1)
        if root.right is not None:
            self.dfs(root.right, 2 * pos + 1, rank + 1)
