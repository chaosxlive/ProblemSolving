# https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

from typing import Optional

# Definition for a rope tree node.


# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        if root.len == 0:
            return root.val[k - 1]

        if root.left:
            if (root.left.len == 0 and len(root.left.val) >= k) or root.left.len >= k:
                return self.getKthCharacter(root.left, k)
            elif root.left.len == 0:
                return self.getKthCharacter(root.right, k - len(root.left.val))
            else:
                return self.getKthCharacter(root.right, k - root.left.len)
        return self.getKthCharacter(root.right, k)
