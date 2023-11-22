# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = [i for i in range(len(stones))]

        def find(x):
            if uf[x] == x:
                return x
            uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return

            if px < py:
                uf[py] = px
            else:
                uf[px] = py

        seenX = {}
        seenY = {}
        for i in range(len(stones)):
            if stones[i][0] not in seenX:
                seenX[stones[i][0]] = i
            if stones[i][1] not in seenY:
                seenY[stones[i][1]] = i

        for i, stone in enumerate(stones):
            if seenX[stone[0]] != i:
                union(i, seenX[stone[0]])
            if seenY[stone[1]] != i:
                union(i, seenY[stone[1]])

        result = 0
        for i in range(len(stones)):
            if uf[i] != i:
                result += 1
        return result
