# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = ListNode()
        leftptr = left
        right = ListNode()
        rightptr = right

        ptr = head
        while ptr != None:
            if ptr.val < x:
                leftptr.next = ptr
                leftptr = leftptr.next
            else:
                rightptr.next = ptr
                rightptr = rightptr.next
            ptr = ptr.next
        
        leftptr.next = right.next
        rightptr.next = None
        return left.next