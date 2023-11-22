# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        ptr = head
        prev = ptr
        cnt = 0
        isDeleting = False
        while ptr is not None:
            if isDeleting:
                prev.next = ptr.next
            else:
                prev = ptr
            cnt += 1
            if isDeleting and cnt == n:
                cnt = 0
                isDeleting = False
            elif not isDeleting and cnt == m:
                cnt = 0
                isDeleting = True
            ptr = ptr.next
        return head
