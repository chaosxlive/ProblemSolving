# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head

        length = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            length += 1

        ptr.next = head
        k = length - (k % length) - 1
        ptr = head
        while k > 0:
            ptr = ptr.next
            k -= 1
        head = ptr.next
        ptr.next = None
        return head
