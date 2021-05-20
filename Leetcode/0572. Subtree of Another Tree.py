# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def isSameTree(root1, root2):
            if root1 == None and root2 == None:
                return True
            if (root1 != None and root2 == None) or (root1 == None and root2 != None):
                return False
            return (root1.val == root2.val) and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

        def dfs(root, subRoot):
            if isSameTree(root, subRoot):
                return True
            if root.left != None and dfs(root.left, subRoot):
                return True
            if root.right != None and dfs(root.right, subRoot):
                return True
            return False

        return dfs(root, subRoot)
