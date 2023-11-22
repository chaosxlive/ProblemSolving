# https://leetcode.com/problems/find-if-path-exists-in-graph/

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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        uf = UnionFind()
        seen = set()
        for u, v in edges:
            seen.add(u)
            seen.add(v)
            uf.union(u, v)
        if source not in seen or destination not in seen:
            return False
        return uf.find(source) == uf.find(destination)
