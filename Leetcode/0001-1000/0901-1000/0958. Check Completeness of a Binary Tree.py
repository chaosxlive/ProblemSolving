# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

from typing import Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        prev = 0
        q = deque()
        q.append((root, 1))
        while q:
            node, idx = q.popleft()
            if idx != prev + 1:
                return False
            prev = idx
            if node.left is not None:
                q.append((node.left, idx * 2))
                if node.right is not None:
                    q.append((node.right, idx * 2 + 1))
            elif node.right is not None:
                return False
        return True
