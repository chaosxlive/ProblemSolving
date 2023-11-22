# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode()
        ptr = result
        ptrList = []
        for index in range(len(lists)):
            if lists[index] != None:
                heapq.heappush(ptrList, [lists[index].val, index, lists[index]])

        magicIndex = len(lists)
        while len(ptrList) > 0:
            next = ptrList[0][2].next
            ptr.next = heapq.heappop(ptrList)[2]
            if next != None:
                heapq.heappush(ptrList, [next.val, magicIndex, next])
            ptr = ptr.next
            magicIndex += 1
        return result.next
