# https://leetcode.com/problems/rank-transform-of-a-matrix/

from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        self.parent.setdefault(u, u)
        self.parent.setdefault(v, v)
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv

    def getGroups(self):
        groups = {}
        for i in self.parent.keys():
            temp = self.find(i)
            if temp not in groups:
                groups[temp] = []
            groups[temp].append(i)
        return groups


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        preSort = defaultdict(list)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                preSort[matrix[row][col]].append((row, col))

        result = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        maxRanks = [0] * (len(matrix) + len(matrix[0]))
        for key in sorted(preSort):
            uf = UnionFind()
            for row, col in preSort[key]:
                uf.union(row, col + len(matrix))
            for group in uf.getGroups().values():
                rank = max(maxRanks[n] for n in group)
                for n in group:
                    maxRanks[n] = rank + 1
            for row, col in preSort[key]:
                result[row][col] = maxRanks[row]
        return result
