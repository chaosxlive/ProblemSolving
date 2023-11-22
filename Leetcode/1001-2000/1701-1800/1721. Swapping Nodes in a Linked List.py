# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        ptr = head
        length = 0
        while ptr != None:
            length += 1
            ptr = ptr.next

        i = 1
        left = min(k, length - k + 1)
        right = max(k, length - k + 1)
        preA = None
        ptrA = head
        while i != left:
            preA = ptrA
            ptrA = ptrA.next
            i += 1
        preB = preA
        ptrB = ptrA
        while i != right:
            preB = ptrB
            ptrB = ptrB.next
            i += 1

        if preA == None:
            if preB == None:
                return head
            preB.next = ptrA
            ptrB.next = ptrA.next
            ptrA.next = None
            return ptrB
        else:
            preA.next = ptrB
            preB.next = ptrA
            temp = ptrA.next
            ptrA.next = ptrB.next
            ptrB.next = temp
            return head
