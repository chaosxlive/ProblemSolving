# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []

        self.result = []
        self.traversal(root)

        return self.result
    
    def traversal(self, root):
        for child in root.children:
            self.traversal(child)
        self.result.append(root.val)