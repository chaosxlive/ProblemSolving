# https://leetcode.com/problems/binary-tree-cameras/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.result = 0
        resultRoot = self.dfs(root)
        return self.result + 1 if resultRoot[2] else self.result

    def dfs(self, root: TreeNode):  # Return [isCamera, isChildCamera, isLeaf]
        if root.left == None and root.right == None:
            return [False, False, True]
        resultLeft = self.dfs(root.left) if root.left != None else [False, False, False]
        resultRight = self.dfs(root.right) if root.right != None else [False, False, False]
        if resultLeft[2] or resultRight[2]:
            self.result += 1
            return [True, False, False]
        if resultLeft[0] or resultRight[0]:
            return [False, True, False]
        return [False, False, True]
