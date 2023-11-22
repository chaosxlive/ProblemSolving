# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def getTotal(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            return root.val + getTotal(root.left) + getTotal(root.right)

        total = getTotal(root)

        def dfs(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return [0, 0]
            leftReslut, leftTotal = dfs(root.left)
            rightResult, rightTotal = dfs(root.right)
            result = max(leftTotal * (total - leftTotal), rightTotal * (total - rightTotal))
            return [max(result, leftReslut, rightResult), root.val + leftTotal + rightTotal]

        return dfs(root)[0] % 1000000007
