# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = right = head
        preLeft = None
        for i in range(n):
            right = right.next
        while right != None:
            right = right.next
            preLeft = left
            left = left.next
        if preLeft != None:
            preLeft.next = left.next
        if left == head:
            head = left.next
        return head
        