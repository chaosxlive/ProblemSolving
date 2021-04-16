# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        prevSlow = nextSlow = None

        while fast != None and fast.next != None:
            fast = fast.next.next
            nextSlow = slow.next
            slow.next = prevSlow
            prevSlow = slow
            slow = nextSlow

        if fast != None:
            slow = slow.next

        while slow != None:
            if slow.val != prevSlow.val:
                return False
            slow = slow.next
            prevSlow = prevSlow.next
        return True
        
