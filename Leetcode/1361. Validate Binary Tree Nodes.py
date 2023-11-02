# https://leetcode.com/problems/validate-binary-tree-nodes/

from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        isChild = [False] * n
        for left in leftChild:
            if left != -1:
                isChild[left] = True
        for right in rightChild:
            if right != -1:
                isChild[right] = True
        root = -1
        for i, b in enumerate(isChild):
            if not b:
                if root != -1:
                    return False
                root = i
        if root == -1:
            return False

        seen = [False] * n

        def dfs(node):
            if seen[node]:
                return False
            seen[node] = True
            if leftChild[node] != -1:
                if not dfs(leftChild[node]):
                    return False
            if rightChild[node] != -1:
                if not dfs(rightChild[node]):
                    return False
            return True

        if not dfs(root):
            return False
        for b in seen:
            if not b:
                return False
        return True
