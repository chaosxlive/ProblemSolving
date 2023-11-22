# https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def dfs(root: TreeNode, num: int):
            if root == None:
                return num
            root.val += dfs(root.right, num)
            return dfs(root.left, root.val)

        dfs(root, 0)
        return root
