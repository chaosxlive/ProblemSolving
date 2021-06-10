# https://leetcode.com/problems/maximum-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        result = root
        ptr, prev = root, None
        while ptr != None:
            if val < ptr.val:
                prev = ptr
                ptr = ptr.right
            else:
                newNode.left = ptr
                if prev != None:
                    prev.right = newNode
                else:
                    result = newNode
                break
        if ptr == None:
            prev.right = newNode
        return result
