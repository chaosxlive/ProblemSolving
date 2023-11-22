# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        self.result = None
        self.val = val
        self.search(root)
        return self.result

    def search(self, root: TreeNode):
        if self.val == root.val:
            self.result = root
            return True
        elif self.val < root.val and root.left != None and self.search(root.left):
            return True
        if self.val > root.val and root.right != None and self.search(root.right):
            return True
        return False
