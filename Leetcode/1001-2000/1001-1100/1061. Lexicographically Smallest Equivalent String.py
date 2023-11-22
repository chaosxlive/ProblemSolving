# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx > ry:
                uf[rx] = ry
            elif rx < ry:
                uf[ry] = rx

        for x, y in zip(s1, s2):
            union(x, y)

        return ''.join([find(c) for c in baseStr])
