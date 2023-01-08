# https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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

        for equation in equations:
            if equation[1] == '=':
                union(equation[0], equation[3])

        for equation in equations:
            if equation[1] == '!':
                if find(equation[0]) == find(equation[3]):
                    return False
        return True
