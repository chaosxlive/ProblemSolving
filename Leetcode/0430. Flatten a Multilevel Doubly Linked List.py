# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head):
        def flatten_child(head):
            ptr, tail = head, None
            while ptr:
                tail = ptr
                if ptr.child:
                    childHead, childTail = flatten_child(ptr.child)
                    tail = childTail
                    ptr.child = None
                    ptrNext = ptr.next
                    ptr.next = childHead
                    childHead.prev = ptr
                    if ptrNext:
                        ptrNext.prev = childTail
                        childTail.next = ptrNext
                ptr = ptr.next
            return head, tail
        result, _ = flatten_child(head)
        return result
