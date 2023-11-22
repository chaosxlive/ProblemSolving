# https://leetcode.com/problems/merge-bsts-to-create-single-bst/

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        candidates = [None] * 50001
        nodePosType = [-1] * 50001
        for tree in trees:
            candidates[tree.val] = [tree, tree.val, tree.val]
            if nodePosType[tree.val] == -1:
                nodePosType[tree.val] = 1
            if tree.left is not None:
                if nodePosType[tree.left.val] == 0:
                    return None
                nodePosType[tree.left.val] = 0
                candidates[tree.val][1] = tree.left.val
            if tree.right is not None:
                if nodePosType[tree.right.val] == 0:
                    return None
                nodePosType[tree.right.val] = 0
                candidates[tree.val][2] = tree.right.val
        resultRoot = None
        for i, t in enumerate(nodePosType):
            if t == 1:
                if resultRoot is not None:
                    return None
                resultRoot = candidates[i][0]
        if resultRoot is None:
            return None
        mergeCnt = 0
        q = deque()
        if resultRoot.left is not None:
            q.append([resultRoot, True, resultRoot.left, -1, resultRoot.val])
        if resultRoot.right is not None:
            q.append([resultRoot, False, resultRoot.right, resultRoot.val, 50001])
        while q:
            parent, isLeft, leaf, minLimit, maxLimit = q.popleft()
            if candidates[leaf.val] is None:
                continue
            leafRoot, leafRootMin, leafRootMax = candidates[leaf.val]
            if leafRootMin <= minLimit:
                return None
            if leafRootMax >= maxLimit:
                return None
            if isLeft:
                parent.left = leafRoot
            else:
                parent.right = leafRoot
            mergeCnt += 1
            if leafRoot.left is not None:
                if isLeft:
                    q.append([leafRoot, True, leafRoot.left, minLimit, leafRoot.val])
                else:
                    q.append([leafRoot, True, leafRoot.left, parent.val, leafRoot.val])
            if leafRoot.right is not None:
                if isLeft:
                    q.append([leafRoot, False, leafRoot.right, leafRoot.val, parent.val])
                else:
                    q.append([leafRoot, False, leafRoot.right, leafRoot.val, maxLimit])
        if mergeCnt < len(trees) - 1:
            return None
        return resultRoot
