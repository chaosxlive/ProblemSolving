# https://leetcode.com/problems/most-frequent-prime/

from collections import defaultdict
from typing import List

PRIMES = [True] * (1000001 + 1)
for p in range(2, 1000001 + 1):
    if PRIMES[p] and PRIMES[p] % 2 == 1:
        PRIMES[p] = True
        for i in range(p * 2, 1000001 + 1, p):
            PRIMES[i] = False


class Solution:

    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        counter = defaultdict(int)
        dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        R = len(mat)
        C = len(mat[0])

        for sri, sr in enumerate(mat):
            for sci, sc in enumerate(sr):
                for dr, dc in dirs:
                    r = sri
                    c = sci
                    curr = sc
                    while 0 <= r + dr < R and 0 <= c + dc < C:
                        r += dr
                        c += dc
                        curr = curr * 10 + mat[r][c]
                        if PRIMES[curr]:
                            counter[curr] += 1
        result = -1
        maxC = 0
        for n, c in counter.items():
            if c > maxC:
                result = n
                maxC = c
            elif c == maxC:
                result = max(result, n)
        return result
