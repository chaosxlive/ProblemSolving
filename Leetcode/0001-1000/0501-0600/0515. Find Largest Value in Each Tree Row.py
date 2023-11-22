# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []

        def dfs(node: TreeNode, level: int):
            if len(result) < level:
                result.append(-2147483648)
            result[level - 1] = max(result[level - 1], node.val)
            if node.left is not None:
                dfs(node.left, level + 1)
            if node.right is not None:
                dfs(node.right, level + 1)

        dfs(root, 1)
        return result
