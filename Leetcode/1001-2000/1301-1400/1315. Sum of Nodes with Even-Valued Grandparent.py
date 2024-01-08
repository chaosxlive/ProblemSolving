# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(node: TreeNode, isPEven: bool, isGPEven: bool):
            if isGPEven:
                self.result += node.val
            isEven = node.val % 2 == 0
            if node.left is not None:
                dfs(node.left, isEven, isPEven)
            if node.right is not None:
                dfs(node.right, isEven, isPEven)

        dfs(root, False, False)

        return self.result
