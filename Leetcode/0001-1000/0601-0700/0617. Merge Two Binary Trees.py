# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None:
            return root2

        def traversal(root1, root2):
            if root2 == None:
                return
            root1.val += root2.val

            if root1.left == None:
                root1.left = root2.left
            else:
                traversal(root1.left, root2.left)
            if root1.right == None:
                root1.right = root2.right
            else:
                traversal(root1.right, root2.right)

        traversal(root1, root2)
        return root1
