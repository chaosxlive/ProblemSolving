# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, num):
        num = (num << 1) + root.val
        if root.left == None and root.right == None:
            self.result += num
            return
        if root.left != None:
            self.dfs(root.left, num)
        if root.right != None:
            self.dfs(root.right, num)
