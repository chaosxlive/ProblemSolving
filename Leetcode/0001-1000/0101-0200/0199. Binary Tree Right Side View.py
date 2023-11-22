# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        self.result = []
        self.traversal(root, 0)
        return self.result

    def traversal(self, root, depth):
        if depth + 1 > len(self.result):
            self.result.append(root.val)
        if root.right != None:
            self.traversal(root.right, depth + 1)
        if root.left != None:
            self.traversal(root.left, depth + 1)
