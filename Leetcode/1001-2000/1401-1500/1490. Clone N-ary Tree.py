# https://leetcode.com/problems/clone-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        node = Node(root.val, [None] * len(root.children))
        for i, child in enumerate(root.children):
            node.children[i] = self.cloneTree(child)
        return node
