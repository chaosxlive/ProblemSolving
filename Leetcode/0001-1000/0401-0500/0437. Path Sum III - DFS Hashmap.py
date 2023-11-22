# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root == None:
            return 0
        self.result = 0
        self.sumList = [0]
        self.target = targetSum

        self.dfs(root)

        return self.result

    def dfs(self, root):
        currentSum = self.sumList[-1] + root.val
        temp = self.sumList.count(currentSum - self.target)
        if temp != 0:
            self.result += temp
        
        self.sumList.append(currentSum)

        if root.left != None:
            self.dfs(root.left)
        if root.right != None:
            self.dfs(root.right)

        self.sumList.pop()