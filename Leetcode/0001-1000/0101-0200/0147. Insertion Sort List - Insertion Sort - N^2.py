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
        ptr = head
        result = ListNode()
        while ptr is not None:
            nextPtr = ptr.next
            val = ptr.val
            finderPrev = result
            finderCurr = result.next
            while finderCurr is not None and finderCurr.val < val:
                finderPrev = finderCurr
                finderCurr = finderCurr.next
            finderPrev.next = ptr
            ptr.next = finderCurr
            ptr = nextPtr
        return result.next
