# https://leetcode.com/problems/linked-list-frequency/

from collections import defaultdict
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for singly-linked list.
    class ListNode:

        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:

    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = defaultdict(int)
        ptr = head
        while ptr is not None:
            cnt[ptr.val] += 1
            ptr = ptr.next
        result = ListNode()
        ptr = result
        for v in cnt.values():
            ptr.next = ListNode(v)
            ptr = ptr.next
        return result.next
