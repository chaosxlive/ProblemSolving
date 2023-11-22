# https://leetcode.com/problems/add-two-numbers-ii/

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = []
        ptr = l1
        while ptr is not None:
            nums1.append(ptr.val)
            ptr = ptr.next
        nums2 = []
        ptr = l2
        while ptr is not None:
            nums2.append(ptr.val)
            ptr = ptr.next
        nums1 = nums1[::-1]
        nums2 = nums2[::-1]
        rest = 0
        result = []
        idx = 0
        while idx < len(nums1) and idx < len(nums2):
            rest += nums1[idx] + nums2[idx]
            result.append(rest % 10)
            rest //= 10
            idx += 1
        while idx < len(nums1):
            rest += nums1[idx]
            result.append(rest % 10)
            rest //= 10
            idx += 1
        while idx < len(nums2):
            rest += nums2[idx]
            result.append(rest % 10)
            rest //= 10
            idx += 1
        while rest:
            result.append(rest % 10)
            rest //= 10
        head = ListNode(result[-1])
        ptr = head
        for i in range(len(result) - 2, -1, -1):
            node = ListNode(result[i])
            ptr.next = node
            ptr = node
        return head
