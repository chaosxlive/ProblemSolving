# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        self.result = []
        self.traversal(root, 0)
        return self.result
        
    def traversal(self, root, level):
        if level >= len(self.result):
            self.result.append([])
        self.result[level].append(root.val)

        if root.left != None:
            self.traversal(root.left, level + 1)
        if root.right != None:
            self.traversal(root.right, level + 1)

