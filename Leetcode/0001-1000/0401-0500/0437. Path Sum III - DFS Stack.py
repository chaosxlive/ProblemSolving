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
        self.target = targetSum
        self.result = 0

        self.dfs(root, [])

        return self.result

    def dfs(self, root, sumList):
        for i in range(len(sumList)):
            sumList[i] += root.val
            if sumList[i] == self.target:
                self.result += 1
        sumList.append(root.val)
        if root.val == self.target:
            self.result += 1

        if root.left != None:
            self.dfs(root.left, sumList[:])
        if root.right != None:
            self.dfs(root.right, sumList[:])
