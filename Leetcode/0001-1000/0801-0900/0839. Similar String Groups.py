# https://leetcode.com/problems/similar-string-groups/

from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def isSimilar(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            diffIdx = [-1, -1]
            for idx, [c1, c2] in enumerate(zip(s1, s2)):
                if c1 != c2:
                    if diffIdx[0] == -1:
                        diffIdx[0] = idx
                    elif diffIdx[1] == -1:
                        diffIdx[1] = idx
                    else:
                        return False
            if diffIdx[0] == diffIdx[1] == -1:
                return True
            if diffIdx[0] == -1 or diffIdx[1] == -1:
                return False
            return s1[diffIdx[0]] == s2[diffIdx[1]] and s1[diffIdx[1]] == s2[diffIdx[0]]

        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry

        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                if isSimilar(strs[i], strs[j]):
                    union(strs[i], strs[j])

        return len(set(find(s) for s in strs))
