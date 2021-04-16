# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ptr = head
        record = []
        while ptr != None:
            record.append(ptr.val)
            ptr = ptr.next
        
        for i in range(len(record) // 2):
            if record[i] != record[-i - 1]:
                return False
        return True
