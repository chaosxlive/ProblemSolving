# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self.search(0, len(nums))

    def search(self, left, right):
        center = (left + right) // 2
        newNode = TreeNode(self.nums[center])
        newNode.left = self.search(left, center) if left < center else None
        newNode.right = self.search(center + 1, right) if center + 1 < right else None
        return newNode
