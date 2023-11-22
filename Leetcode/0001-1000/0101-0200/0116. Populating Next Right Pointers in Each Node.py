# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(root, prevRight):
            if root is None:
                return
            root.next = prevRight
            dfs(root.left, root.right)
            dfs(root.right, prevRight.left if prevRight is not None else None)

        dfs(root, None)
        return root
