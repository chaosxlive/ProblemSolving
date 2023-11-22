# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, -2147483648)
        return self.result

    def dfs(self, node: TreeNode, prevMax: int):
        if node.val >= prevMax:
            self.result += 1
        if node.left != None:
            self.dfs(node.left, max(node.val, prevMax))
        if node.right != None:
            self.dfs(node.right, max(node.val, prevMax))
