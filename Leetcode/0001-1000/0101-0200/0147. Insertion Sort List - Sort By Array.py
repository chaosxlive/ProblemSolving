# https://leetcode.com/problems/insertion-sort-list/

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next: Optional['ListNode'] = None):
            self.val = val
            self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        ptr = head
        while ptr is not None:
            nums.append(ptr.val)
            ptr = ptr.next
        nums.sort()
        result = ListNode()
        ptr = result
        for num in nums:
            n = ListNode(num)
            ptr.next = n
            ptr = n
        return result.next
