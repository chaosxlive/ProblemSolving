# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.getPreorder(root)
        return self.result

    def getPreorder(self, root):
        if root == None:
            return
        
        self.result.append(root.val)

        for child in root.children:
            self.getPreorder(child)
        
