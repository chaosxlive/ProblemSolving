# https://leetcode.com/problems/smallest-string-starting-from-leaf/

from string import ascii_lowercase
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    leaves = []

    def findLeaves(self, path, root):
        if root is None:
            return
        path.append(ascii_lowercase[root.val])
        if root.left is None and root.right is None:
            self.leaves.append(''.join(path[::-1]))
        if root.left:
            self.findLeaves(path, root.left)
        if root.right:
            self.findLeaves(path, root.right)
        path.pop()

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.leaves.clear()
        self.findLeaves([], root)
        return min(self.leaves)
