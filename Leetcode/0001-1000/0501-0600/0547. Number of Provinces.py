# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry

        l = len(isConnected)
        for i in range(l):
            for j in range(i, l):
                if isConnected[i][j]:
                    union(i, j)
        s = set()
        for i in range(l):
            s.add(find(i))
        return len(s)
