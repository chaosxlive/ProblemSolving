# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        def getTail(node, k):
            ptr = node
            count = 1
            while ptr != None and count != k:
                ptr = ptr.next
                count += 1
            return ptr if count == k else None

        tail = getTail(head, k)
        if tail == None:
            return head

        def reverseList(start, end, prevGroup=None):
            ptr, prev, endpoint = start, None, end.next
            while ptr != endpoint:
                next = ptr.next

                ptr.next = prev
                prev = ptr
                ptr = next
            if prevGroup:
                prevGroup.next = end
            start.next = next
            return end, start, next

        head, prev, next = reverseList(head, tail)

        while True:
            tail = getTail(next, k)
            if tail == None:
                return head
            start, prev, next = reverseList(next, tail, prev)
