# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def traverse(root):
            if root.left and traverse(root.left):
                root.left = None
            if root.right and traverse(root.right):
                root.right = None

            return root.val == 0 and root.left == None and root.right == None

        traverse(root)
        return None if root.val == 0 and root.left == None and root.right == None else root
