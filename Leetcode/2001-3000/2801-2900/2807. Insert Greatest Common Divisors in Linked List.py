# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

from typing import Optional
from math import gcd


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next: Optional['ListNode'] = None):
#         self.val = val
#         self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head.next
        while b is not None:
            mid = gcd(a.val, b.val)
            a.next = ListNode(mid, b)
            a = b
            b = b.next
        return head
