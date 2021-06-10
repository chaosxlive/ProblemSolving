# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.traversal(root)
        return self.result

    def traversal(self, root):
        if root == None:
            return
        self.traversal(root.left)
        self.result.append(root.val)
        self.traversal(root.right)
