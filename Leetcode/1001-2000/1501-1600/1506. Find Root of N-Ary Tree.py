# https://leetcode.com/problems/find-root-of-n-ary-tree/

from typing import List


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        hasParent = {}
        nodeMap = {}
        for node in tree:
            if node.val not in hasParent:
                nodeMap[node.val] = node
                hasParent[node.val] = False
            for child in node.children:
                if child not in hasParent:
                    nodeMap[child.val] = node
                    hasParent[child.val] = True
                else:
                    hasParent[child.val] = True
        for v, isHP in hasParent.items():
            if not isHP:
                return nodeMap[v]
        return None
