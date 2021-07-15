# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        tree = TreeNode(preorder[0])

        def addBSTNode(root, num):
            if num < root.val:
                if root.left == None:
                    root.left = TreeNode(num)
                else:
                    addBSTNode(root.left, num)
            else:
                if root.right == None:
                    root.right = TreeNode(num)
                else:
                    addBSTNode(root.right, num)

        for num in preorder[1:]:
            addBSTNode(tree, num)
        return tree
