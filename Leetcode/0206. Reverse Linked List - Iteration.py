# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ptr, ptrPrev = head, None
        while ptr != None:
            ptrNext = ptr.next
            ptr.next = ptrPrev
            ptrPrev = ptr
            ptr = ptrNext
        return ptrPrev
