# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        deleted = set()
        ptr, ptrPrev = head, None
        while ptr != None:
            if ptr.val in deleted:
                if ptr == head:
                    head = ptr.next
                else:
                    ptrPrev.next = ptr.next
                ptr = ptr.next
            else:
                if ptr.next != None and ptr.val == ptr.next.val:
                    deleted.add(ptr.val)
                else:
                    ptrPrev = ptr
                    ptr = ptr.next
        return head
