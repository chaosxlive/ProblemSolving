# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.parentX = self.parentY = None
        self.depthX = self.depthY = -1
        self.x = x
        self.y = y

        self.dfs(0, None, root)

        return self.depthX == self.depthY and self.parentX != self.parentY

    def dfs(self, depth, parent, root):
        if root == None:
            return
        if root.val == self.x:
            self.parentX = parent
            self.depthX = depth
        elif root.val == self.y:
            self.parentY = parent
            self.depthY = depth

        if root.left != None:
            self.dfs(depth + 1, root, root.left)
        if root.right != None:
            self.dfs(depth + 1, root, root.right)
