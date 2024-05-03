from collections import defaultdict
from functools import cache
from math import inf


class Solution:

    def findRotateSteps(self, ring: str, key: str) -> int:
        L = len(ring)
        KL = len(key)
        WORDS = ring * 3

        idxs = defaultdict(list)
        for i, c in enumerate(WORDS):
            idxs[c].append(i)

        @cache
        def solve(wi, ki):
            if ki == KL:
                return 0
            res = inf
            for i in idxs[key[ki]]:
                res = min(res, solve((i % L) + L, ki + 1) + abs(i - wi))
            return res

        return solve(L, 0) + KL
