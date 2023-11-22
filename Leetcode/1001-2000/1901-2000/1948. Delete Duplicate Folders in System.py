# https://leetcode.com/problems/delete-duplicate-folders-in-system/

from collections import Counter


class Solution:

    class TreeNode:

        def __init__(self):
            self.children = {}
            self.signature = None

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = self.TreeNode()

        for path in paths:
            ptr = tree
            for p in path:
                if p not in ptr.children:
                    ptr.children[p] = self.TreeNode()
                ptr = ptr.children[p]

        counter = Counter()

        def getSignature(node):
            buffer = []
            for childKey in sorted(node.children):
                buffer.append((childKey, getSignature(node.children[childKey])))
            node.signature = hash(tuple(buffer))
            if len(buffer):
                counter[node.signature] += 1
            return node.signature

        getSignature(tree)

        result = []
        currentPath = []

        def traverse(node):
            if counter[node.signature] >= 2:
                return
            if len(currentPath):
                result.append(currentPath[:])
            for childKey in sorted(node.children):
                currentPath.append(childKey)
                traverse(node.children[childKey])
                currentPath.pop()
        traverse(tree)
        return result
