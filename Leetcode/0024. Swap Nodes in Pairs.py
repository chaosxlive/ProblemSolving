# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        def getTail(node, k):
            ptr = node
            count = 1
            while ptr != None and count != k:
                ptr = ptr.next
                count += 1
            return ptr if count == k else None

        tail = getTail(head, 2)
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
            tail = getTail(next, 2)
            if tail == None:
                return head
            start, prev, next = reverseList(next, tail, prev)
