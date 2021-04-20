# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root == None:
            return []

        self.targetSum = targetSum
        self.result = []

        self.dfs(root, [], 0)

        return self.result

    def dfs(self, root, prevPath, prevSum):
        currentSum = prevSum + root.val
        currentPath = prevPath + [root.val]
        if root.left == None and root.right == None and currentSum == self.targetSum:
            self.result.append(currentPath[:])
            return

        if root.left:
            self.dfs(root.left, currentPath, currentSum)
        if root.right:
            self.dfs(root.right, currentPath, currentSum)
