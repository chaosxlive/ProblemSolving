# https://leetcode.com/problems/plus-one-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        lastNotNine = None
        ptr = head
        while ptr is not None:
            if ptr.val != 9:
                lastNotNine = ptr
            ptr = ptr.next
        if lastNotNine is None:
            result = ListNode(1, head)
            ptr = head
        else:
            result = head
            lastNotNine.val += 1
            ptr = lastNotNine.next
        while ptr is not None:
            ptr.val = 0
            ptr = ptr.next
        return result
