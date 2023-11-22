# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        stack = []
        while fast is not None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        result = 0
        while slow is not None:
            result = max(result, slow.val + stack[-1])
            stack.pop()
            slow = slow.next
        return result
