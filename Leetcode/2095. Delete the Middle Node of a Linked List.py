# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        slowPrev = None

        while fast != None and fast.next != None:
            slowPrev = slow
            slow = slow.next
            fast = fast.next.next

        if slowPrev == None:
            return None
        slowPrev.next = slow.next
        return head
