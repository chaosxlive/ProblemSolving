# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        self.targetSum = targetSum
        return self.dfs(root, 0)

    def dfs(self, root, prevSum):
        currentSum = prevSum + root.val
        if root.left == None and root.right == None:
            if currentSum == self.targetSum:
                return True
            else:
                return False
        
        if root.left != None and self.dfs(root.left, currentSum):
            return True
        if root.right != None and self.dfs(root.right, currentSum):
            return True
        return False
        
            
