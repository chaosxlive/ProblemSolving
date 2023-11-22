# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA = headA
        ptrB = headB
        visited = set()
        while ptrA != None and ptrB != None:
            if ptrA in visited:
                return ptrA
            visited.add(ptrA)
            if ptrB in visited:
                return ptrB
            visited.add(ptrB)
            ptrA = ptrA.next
            ptrB = ptrB.next
        while ptrA != None:
            if ptrA in visited:
                return ptrA
            ptrA = ptrA.next
        while ptrB != None:
            if ptrB in visited:
                return ptrB
            ptrB = ptrB.next
        return None
