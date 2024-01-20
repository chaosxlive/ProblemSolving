# https://leetcode.com/problems/stone-game-v/

from itertools import accumulate
from typing import List


class Solution:

    def stoneGameV(self, stoneValue: List[int]) -> int:
        acc = [0, *accumulate(stoneValue)]
        L = len(stoneValue)
        result = [[0] * L for _ in range(L)]
        leftMax = [[0] * L for _ in range(L)]
        rightMax = [[0] * L for _ in range(L)]
        crit = [[0] * L for _ in range(L)]

        for start in range(L):
            s = 0
            ptr = start
            for end in range(start + 1, L):
                t = acc[end + 1] - acc[start]
                while ptr <= end and (s + stoneValue[ptr]) * 2 <= t:
                    s += stoneValue[ptr]
                    ptr += 1
                crit[start][end] = ptr - 1

        for l in range(1, L + 1):
            for start in range(L):
                end = start + l - 1
                if end >= L:
                    continue
                if l == 1:
                    leftMax[start][end] = rightMax[start][end] = stoneValue[start]
                    continue
                t = acc[end + 1] - acc[start]
                if start <= crit[start][end]:
                    result[start][end] = max(result[start][end], leftMax[start][crit[start][end]])
                    left = acc[crit[start][end] + 1] - acc[start]
                    if left * 2 == t:
                        result[start][end] = max(result[start][end], rightMax[crit[start][end] + 1][end])
                if crit[start][end] + 1 < end:
                    result[start][end] = max(result[start][end], rightMax[crit[start][end] + 2][end])

                leftMax[start][end] = max(leftMax[start][end - 1], result[start][end] + t)
                rightMax[start][end] = max(rightMax[start + 1][end], result[start][end] + t)

        return result[0][L - 1]
