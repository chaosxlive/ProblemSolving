# https://leetcode.com/problems/find-bottom-left-tree-value/

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

    def findBottomLeftValue(self, root: Optional['TreeNode']) -> int:
        q = deque([(root, 0)])
        resultVal = root.val
        resultLevel = 0
        while q:
            node, level = q.popleft()
            if level > resultLevel:
                resultVal = node.val
                resultLevel = level
            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))
        return resultVal
