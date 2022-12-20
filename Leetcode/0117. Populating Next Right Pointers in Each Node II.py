# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

from collections import deque


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
    def connect(self, root: 'Node') -> 'Node':
        nextQ = deque([root])
        while len(nextQ) > 0:
            q = nextQ
            nextQ = deque()
            while len(q) > 0:
                node = q.popleft()
                if node is None:
                    continue
                while len(q) > 0:
                    if q[0] is None:
                        q.popleft()
                    else:
                        node.next = q[0]
                        break
                nextQ.append(node.left)
                nextQ.append(node.right)
        return root
