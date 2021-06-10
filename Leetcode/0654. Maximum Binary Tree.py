# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        tree = TreeNode(nums[0])
        for index in range(1, len(nums)):
            newNode = TreeNode(nums[index])
            ptr, prev = tree, None
            while ptr != None:
                if nums[index] < ptr.val:
                    prev = ptr
                    ptr = ptr.right
                else:
                    newNode.left = ptr
                    if prev != None:
                        prev.right = newNode
                    else:
                        tree = newNode
                    break
            if ptr == None:
                prev.right = newNode
        return tree
