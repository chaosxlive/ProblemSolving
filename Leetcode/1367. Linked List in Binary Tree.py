# https://leetcode.com/problems/linked-list-in-binary-tree/

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(treeNode: Optional[TreeNode]):
            if treeNode is None:
                return False

            def check(treeNode: TreeNode, listNode: ListNode):
                if treeNode.val != listNode.val:
                    return False
                if listNode.next is None:
                    return True
                if treeNode.left is not None and check(treeNode.left, listNode.next):
                    return True
                if treeNode.right is not None and check(treeNode.right, listNode.next):
                    return True
                return False

            if check(treeNode, head):
                return True
            if treeNode.left is not None and dfs(treeNode.left):
                return True
            if treeNode.right is not None and dfs(treeNode.right):
                return True
            return False

        return dfs(root)
