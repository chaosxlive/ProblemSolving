# https://leetcode.com/problems/find-all-the-lonely-nodes/

from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for a binary tree node.
    class TreeNode:

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:

    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def dfs(result: List[int], root: Optional[TreeNode], isAns: bool):
            if root is None:
                return
            if isAns:
                result.append(root.val)
            if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
                dfs(result, root.left, True)
                dfs(result, root.right, True)
            else:
                dfs(result, root.left, False)
                dfs(result, root.right, False)

        dfs(result, root, False)

        return result
