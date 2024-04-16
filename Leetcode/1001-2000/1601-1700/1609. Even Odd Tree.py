# https://leetcode.com/problems/even-odd-tree/

from collections import deque
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, 0)])
        cached = [None] * (10**5)
        while q:
            node, level = q.popleft()
            if level % 2 == 0:
                if node.val % 2 == 0:
                    return False
            else:
                if node.val % 2 > 0:
                    return False

            if cached[level] is None:
                cached[level] = node.val
            else:
                if level % 2 == 0:
                    if node.val <= cached[level]:
                        return False
                else:
                    if node.val >= cached[level]:
                        return False
                cached[level] = node.val
            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))
        return True
