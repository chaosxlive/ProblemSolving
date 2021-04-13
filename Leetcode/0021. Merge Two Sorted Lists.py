# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        preResult = ListNode()
        iter1 = l1
        iter2 = l2
        iterResult = preResult

        while iter1 != None and iter2 != None:
            if iter1.val < iter2.val:
                iterResult.next = iter1
                iter1 = iter1.next
            else:
                iterResult.next = iter2
                iter2 = iter2.next
            iterResult = iterResult.next

        while iter1 != None:
            iterResult.next = iter1
            iter1 = iter1.next
            iterResult = iterResult.next
            
        while iter2 != None:
            iterResult.next = iter2
            iter2 = iter2.next
            iterResult = iterResult.next
        
        return preResult.next
