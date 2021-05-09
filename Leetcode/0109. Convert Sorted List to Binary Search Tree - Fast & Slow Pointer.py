# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        return self.search(head, None)

    def search(self, left, right):
        if left == right:
            return None
        slow = fast = left

        while fast.next != right and fast.next.next != right:
            slow = slow.next
            fast = fast.next.next

        newNode = TreeNode(slow.val)
        newNode.left = self.search(left, slow)
        newNode.right = self.search(slow.next, right)
        return newNode
