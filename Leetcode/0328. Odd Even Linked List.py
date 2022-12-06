# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headOdd = ListNode()
        ptrOdd = headOdd
        headEven = ListNode()
        ptrEven = headEven
        ptr = head
        idx = 0
        while ptr != None:
            if idx % 2 == 0:
                ptrEven.next = ptr
                ptrEven = ptr
            else:
                ptrOdd.next = ptr
                ptrOdd = ptr
            nextNode = ptr.next
            ptr.next = None
            ptr = nextNode
            idx += 1
        if ptrEven == headEven:
            return None
        if ptrOdd == headOdd:
            return head
        ptrEven.next = headOdd.next
        return headEven.next
