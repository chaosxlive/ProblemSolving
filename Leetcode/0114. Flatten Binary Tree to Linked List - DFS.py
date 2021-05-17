# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root: TreeNode) -> TreeNode:
            nodeLeft = root.left
            nodeRight = root.right
            if nodeLeft == None and nodeRight == None:
                return root
            elif nodeLeft != None and nodeRight == None:
                root.right = nodeLeft
                root.left = None
                return dfs(nodeLeft)
            elif nodeLeft == None and nodeRight != None:
                return dfs(nodeRight)
            else:
                root.right = nodeLeft
                root.left = None
                nodeLeftEnd = dfs(nodeLeft)
                nodeLeftEnd.right = nodeRight
                return dfs(nodeRight)

        if root == None:
            return

        dfs(root)
        return
