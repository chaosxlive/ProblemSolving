# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ptr = head
        result = 0
        while ptr != None:
            result <<= 1
            if ptr.val == 1:
                result += 1
            ptr = ptr.next
        
        return result