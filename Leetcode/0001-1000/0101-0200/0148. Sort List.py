# https://leetcode.com/problems/sort-list/

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = []
        ptr = head
        while ptr is not None:
            nodes.append((ptr.val, ptr))
            ptr = ptr.next
        nodes.sort(key=lambda x: x[0])
        result = nodes[0][1]
        result.next = None
        ptr = result
        for i in range(1, len(nodes)):
            ptr.next = nodes[i][1]
            ptr = ptr.next
            ptr.next = None
        return result
