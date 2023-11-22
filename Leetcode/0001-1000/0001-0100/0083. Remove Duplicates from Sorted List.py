# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        ptr, ptrPrev = head.next, head
        while ptr != None:
            if ptr.val == ptrPrev.val:
                ptrPrev.next = ptr.next
            else:
                ptrPrev = ptr
            ptr = ptr.next
        return head
