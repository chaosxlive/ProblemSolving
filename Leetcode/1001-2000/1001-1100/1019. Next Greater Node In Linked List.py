# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        val_stack = []
        idx_stack = []
        result = []

        iter_node = head
        iter_index = 0
        while iter_node != None:
            while len(val_stack) != 0 and val_stack[-1] < iter_node.val:
                result[idx_stack[-1]] = iter_node.val
                val_stack.pop()
                idx_stack.pop()

            val_stack.append(iter_node.val)
            idx_stack.append(iter_index)
            result.append(0)

            iter_index += 1
            iter_node = iter_node.next

        return result
        