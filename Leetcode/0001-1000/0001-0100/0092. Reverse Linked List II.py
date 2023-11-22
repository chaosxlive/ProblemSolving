# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        count = 1
        ptr, ptrPrev = head, None
        while count < left:
            ptrPrev = ptr
            ptr = ptr.next
            count += 1

        firstRev = ptr
        firstRevPrev = ptrPrev

        while count <= right:
            ptrNext = ptr.next
            ptr.next = ptrPrev
            ptrPrev = ptr
            ptr = ptrNext
            count += 1

        if firstRevPrev != None:
            firstRev.next = ptr
            firstRevPrev.next = ptrPrev
        else:
            head.next = ptr
            return ptrPrev

        return head
