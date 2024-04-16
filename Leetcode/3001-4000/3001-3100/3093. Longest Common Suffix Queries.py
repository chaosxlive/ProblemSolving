# https://leetcode.com/problems/longest-common-suffix-queries/

from typing import List


class PrefixTreeNode:

    def __init__(self, idx=-1) -> None:
        self.idx = idx
        self.children = {}


class Solution:

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        result = [0] * len(wordsQuery)

        lbi = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[lbi]):
                lbi = i

        root = PrefixTreeNode(lbi)
        for i, w in enumerate(map(lambda x: x[::-1], wordsContainer)):
            ptr = root
            L = len(w)
            for c in w:
                if c not in ptr.children:
                    ptr.children[c] = PrefixTreeNode(i)
                ptr = ptr.children[c]
                if L < len(wordsContainer[ptr.idx]):
                    ptr.idx = i

        for i, q in enumerate(map(lambda x: x[::-1], wordsQuery)):
            ptr = root
            for c in q:
                if c not in ptr.children:
                    break
                ptr = ptr.children[c]
            result[i] = ptr.idx

        return result
