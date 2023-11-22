# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        result = 0
        for child in root.children:
            result = max(self.maxDepth(child), result)
        return result + 1
