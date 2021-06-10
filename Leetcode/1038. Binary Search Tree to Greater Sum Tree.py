# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def dfs(root: TreeNode, num: int):
            if root == None:
                return num
            root.val += dfs(root.right, num)
            return dfs(root.left, root.val)

        dfs(root, 0)
        return root
