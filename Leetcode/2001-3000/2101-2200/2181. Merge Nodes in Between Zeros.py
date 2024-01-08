# https://leetcode.com/problems/merge-nodes-in-between-zeros/

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()

        it = head
        rit = result
        while True:
            if it.val == 0:
                if it.next is None:
                    break
                rit.next = ListNode()
                rit = rit.next
            else:
                rit.val += it.val
            it = it.next

        return result.next