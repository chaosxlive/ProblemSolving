# https://leetcode.com/problems/reorder-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        slow = slow.next
        prev.next = None
        stack = []
        while slow is not None:
            stack.append(slow)
            slow = slow.next
            stack[-1].next = None
        slow = head
        fast = head.next
        while len(stack) > 0:
            node = stack.pop()
            slow.next = node
            node.next = fast
            slow = fast
            if fast is not None:
                fast = fast.next
        return head
