# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def find(nodeOrigin: TreeNode, nodeCloned: TreeNode, target: int) -> TreeNode:
            if nodeOrigin.val == target:
                return nodeCloned
            temp = None
            if nodeOrigin.left is not None:
                temp = find(nodeOrigin.left, nodeCloned.left, target)
                if temp is not None:
                    return temp
            if nodeOrigin.right is not None:
                temp = find(nodeOrigin.right, nodeCloned.right, target)
                if temp is not None:
                    return temp
            return None

        return find(original, cloned, target.val)
