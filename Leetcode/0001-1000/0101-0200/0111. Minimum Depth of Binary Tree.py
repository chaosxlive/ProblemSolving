# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from queue import Queue


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        next = Queue()
        next.put((root, 1))
        while True:
            node, depth = next.get()
            if node.left == None and node.right == None:
                return depth
            if node.left != None:
                next.put((node.left, depth + 1))
            if node.right != None:
                next.put((node.right, depth + 1))
