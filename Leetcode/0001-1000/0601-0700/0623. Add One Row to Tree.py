# https://leetcode.com/problems/add-one-row-to-tree/

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

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        dq = deque([(root, 1)])
        depth -= 1
        while dq:
            n, d = dq.popleft()
            if d == depth:
                n.left = TreeNode(val, left=n.left)
                n.right = TreeNode(val, right=n.right)
            else:
                if n.left is not None:
                    dq.append((n.left, d + 1))
                if n.right is not None:
                    dq.append((n.right, d + 1))
        return root
