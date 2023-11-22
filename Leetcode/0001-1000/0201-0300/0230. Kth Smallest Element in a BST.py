# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = -1
        self.target = k
        self.dfs(root, 0)
        return self.result

    def dfs(self, root: Optional[TreeNode], count: int) -> int:
        if root is None:
            return count
        count = self.dfs(root.left, count)
        if count == self.target:
            return count
        count += 1
        if count == self.target:
            self.result = root.val
            return count
        count = self.dfs(root.right, count)
        if count == self.target:
            return count
        return count
