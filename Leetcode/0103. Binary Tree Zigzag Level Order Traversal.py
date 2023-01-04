# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = deque([(root, 1)])
        while q:
            node, rank = q.popleft()
            if len(result) < rank:
                result.append([])
            result[-1].append(node.val)
            if node.left is not None:
                q.append((node.left, rank + 1))
            if node.right is not None:
                q.append((node.right, rank + 1))
        return list(map(lambda x: x[1] if x[0] % 2 == 0 else x[1][::-1], enumerate(result)))
