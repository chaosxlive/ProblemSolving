# https://leetcode.com/problems/linked-list-random-node/description/

import random
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        n = 1
        picked = 0
        ptr = self.head
        while ptr is not None:
            if random.random() < 1 / n:
                picked = ptr.val
            ptr = ptr.next
            n += 1
        return picked


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
