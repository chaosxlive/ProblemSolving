# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = TreeNode()
        self.tail = self.head

        self.dfs(root)

        return self.head.right

    def dfs(self, root):
        if root.left != None:
            self.dfs(root.left)
        root.left = None

        self.tail.right = root
        self.tail = self.tail.right

        if root.right != None:
            self.dfs(root.right)
