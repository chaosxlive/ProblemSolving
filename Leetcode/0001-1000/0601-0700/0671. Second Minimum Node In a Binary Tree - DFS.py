# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min1 = self.min2 = None

        def dfs(root):
            if root is None:
                return
            if self.min1 is None:
                self.min1 = root.val
            else:
                if root.val < self.min1:
                    self.min2 = self.min1
                    self.min1 = root.val
                elif root.val > self.min1:
                    if self.min2 is None or root.val < self.min2:
                        self.min2 = root.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return -1 if self.min2 is None else self.min2
