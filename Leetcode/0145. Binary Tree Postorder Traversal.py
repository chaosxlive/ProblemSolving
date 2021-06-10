# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []
        self.traversal(root)
        return self.result

    def traversal(self, root):
        if root == None:
            return
        self.traversal(root.left)
        self.traversal(root.right)
        self.result.append(root.val)
