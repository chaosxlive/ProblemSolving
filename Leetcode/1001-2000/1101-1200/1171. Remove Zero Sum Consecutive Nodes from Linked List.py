# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for singly-linked list.
    class ListNode:

        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, head)
        ptr = head
        s = 0
        seen = {0: result}
        marked = set()
        while ptr is not None:
            s += ptr.val
            if s in seen and seen[s] not in marked:
                r = seen[s].next
                while r is not None and r != ptr and r not in marked:
                    marked.add(r)
                    r = r.next
                marked.add(ptr)
                seen[s].next = ptr.next
            else:
                seen[s] = ptr
            ptr = ptr.next
        return result.next
