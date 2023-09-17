# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.levels = defaultdict(int)
        self.dfs(root, 1)
        return sorted(self.levels.items(), key=lambda x: [-x[1], x[0]])[0][0]

    def dfs(self, node: Optional[TreeNode], level: int):
        if node == None:
            return
        self.levels[level] += node.val
        self.dfs(node.left, level+1)
        self.dfs(node.right, level + 1)
