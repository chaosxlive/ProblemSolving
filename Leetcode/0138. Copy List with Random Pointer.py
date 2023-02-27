# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional


# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        oldToNew = {}
        newHead = Node(head.val)
        oldToNew[id(None)] = None
        oldToNew[id(head)] = newHead
        newPrev = newHead
        ptr = head.next
        while ptr is not None:
            newNode = Node(ptr.val)
            newPrev.next = newNode
            oldToNew[id(ptr)] = newNode
            newPrev = newNode
            ptr = ptr.next
        ptrOld = head
        ptrNew = newHead
        while ptrOld is not None:
            ptrNew.random = oldToNew[id(ptrOld.random)]
            ptrOld = ptrOld.next
            ptrNew = ptrNew.next
        return newHead
