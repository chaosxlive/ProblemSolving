# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ptr, ptrPrev = head, None
        while ptr != None:
            if ptr.val == val:
                if ptr == head:
                    head = ptr.next
                    ptr = ptr.next
                else:
                    ptrPrev.next = ptr.next
                    ptr = ptr.next
            else:
                ptrPrev = ptr
                ptr = ptr.next
        return head
