# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        preResult = ListNode()
        carry = 0
        iter1 = l1
        iter2 = l2
        iterResult = preResult
        while iter1 != None and iter2 != None:
            tempNode = ListNode((iter1.val + iter2.val + carry) % 10)
            carry = (iter1.val + iter2.val + carry) // 10
            iterResult.next = tempNode
            iterResult = iterResult.next
            iter1 = iter1.next
            iter2 = iter2.next
        
        while iter1 != None:
            tempNode = ListNode((iter1.val + carry) % 10)
            carry = (iter1.val + carry) // 10
            iterResult.next = tempNode
            iterResult = iterResult.next
            iter1 = iter1.next

        while iter2 != None:
            tempNode = ListNode((iter2.val + carry) % 10)
            carry = (iter2.val + carry) // 10
            iterResult.next = tempNode
            iterResult = iterResult.next
            iter2 = iter2.next

        if carry != 0:
            iterResult.next = ListNode(carry)
        
        return preResult.next
