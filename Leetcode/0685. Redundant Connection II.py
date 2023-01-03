# https://leetcode.com/problems/redundant-connection-ii/

from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
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

        nodeCnt = len(edges)
        parent = [-1] * (nodeCnt + 1)
        doubleParent = None
        for start, end in edges:
            if parent[end] != -1:
                doubleParent = [end, parent[end], start]
            parent[end] = start
            union(end, start)
        for n in range(1, nodeCnt + 1):
            find(n)
        if doubleParent is None:
            return [parent[find(1)], find(1)]

        def dfs(node, doubleParentNode):
            parentNode = parent[node]
            if parentNode == -1:
                return False
            if parentNode == doubleParentNode:
                return True
            return dfs(parentNode, doubleParentNode)

        return [doubleParent[1] if dfs(doubleParent[1], doubleParent[0]) else doubleParent[2], doubleParent[0]]
