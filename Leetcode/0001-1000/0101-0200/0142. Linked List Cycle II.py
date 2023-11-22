# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        ptr = head
        while True:
            if ptr is None:
                return None
            if id(ptr) in seen:
                return ptr
            seen.add(id(ptr))
            ptr = ptr.next
