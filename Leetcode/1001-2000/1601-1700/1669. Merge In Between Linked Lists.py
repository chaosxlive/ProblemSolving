# https://leetcode.com/problems/merge-in-between-linked-lists/

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for singly-linked list.
    class ListNode:

        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        ptr = list1
        while i < a - 1:
            ptr = ptr.next
            i += 1
        temp = ptr
        while i <= b:
            ptr = ptr.next
            i += 1
        temp.next = list2
        while temp.next is not None:
            temp = temp.next
        temp.next = ptr
        return list1
