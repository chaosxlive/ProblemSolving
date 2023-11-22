# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = (x, 1.0)
            elif uf[x][0] != x:
                root = find(uf[x][0])
                uf[x] = (root[0], uf[x][1] * root[1])
            return uf[x]

        def union(x, y, m):
            rootX = find(x)
            rootY = find(y)
            if rootX[0] != rootY[0]:
                uf[rootX[0]] = (rootY[0], m * rootY[1] / rootX[1])

        for idx, (a, b) in enumerate(equations):
            val = values[idx]
            union(a, b, val)

        result = []
        for a, b in queries:
            if a not in uf or b not in uf:
                result.append(-1.0)
            else:
                rootA = find(a)
                rootB = find(b)
                if rootA[0] != rootB[0]:
                    result.append(-1.0)
                else:
                    result.append(rootA[1] / rootB[1])
        return result
