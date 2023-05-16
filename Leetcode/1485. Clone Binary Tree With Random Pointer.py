# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

from typing import Optional


# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


# class NodeCopy(Node):
#     pass


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if root is None:
            return None
        
        idMap = {}

        def dfs(node: Node, newNode: NodeCopy):
            newNode.val = node.val
            if node.left is not None:
                if id(node.left) in idMap:
                    newNode.left = idMap[id(node.left)]
                else:
                    newNode.left = NodeCopy()
                    idMap[id(node.left)] = newNode.left
                dfs(node.left, newNode.left)
            if node.right is not None:
                if id(node.right) in idMap:
                    newNode.right = idMap[id(node.right)]
                else:
                    newNode.right = NodeCopy()
                    idMap[id(node.right)] = newNode.right
                dfs(node.right, newNode.right)
            if node.random is not None:
                if id(node.random) in idMap:
                    newNode.random = idMap[id(node.random)]
                else:
                    newNode.random = NodeCopy()
                    idMap[id(node.random)] = newNode.random

        newRoot = NodeCopy()
        idMap[id(root)] = newRoot
        dfs(root, newRoot)
        return newRoot
