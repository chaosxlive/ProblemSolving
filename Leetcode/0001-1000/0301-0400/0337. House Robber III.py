# https://leetcode.com/problems/house-robber-iii/

from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root: TreeNode) -> List[int]:
            leftTake = leftSkip = rightTake = rightSkip = 0
            if root.left:
                leftTake, leftSkip = dfs(root.left)
            if root.right:
                rightTake, rightSkip = dfs(root.right)

            return [root.val + leftSkip + rightSkip, max(leftTake, leftSkip) + max(rightTake, rightSkip)]  # Take root, Skip root

        return max(dfs(root))
