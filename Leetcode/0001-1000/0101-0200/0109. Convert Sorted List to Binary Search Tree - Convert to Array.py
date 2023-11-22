# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.nums = []
        ptr = head
        while ptr != None:
            self.nums.append(ptr.val)
            ptr = ptr.next
        if len(self.nums) == 0:
            return None
        return self.search(0, len(self.nums))

    def search(self, left, right):
        center = (left + right) // 2
        newNode = TreeNode(self.nums[center])
        newNode.left = self.search(left, center) if left < center else None
        newNode.right = self.search(center + 1, right) if center + 1 < right else None
        return newNode
