# https://leetcode.com/problems/winner-of-the-linked-list-game/

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:

    # Definition for singly-linked list.
    class ListNode:

        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:

    def gameResult(self, head: Optional[ListNode]) -> str:
        diff = 0
        ptrEven = head
        ptrOdd = head.next
        while True:
            if ptrEven.val > ptrOdd.val:
                diff += 1
            else:
                diff -= 1
            ptrEven = ptrOdd.next
            if ptrEven is None:
                break
            ptrOdd = ptrEven.next
        if diff > 0:
            return "Even"
        elif diff < 0:
            return "Odd"
        else:
            return "Tie"
