# https://leetcode.com/problems/greatest-common-divisor-traversal/

from typing import List

PRIME_LEN = 10**5
IS_PRIME = [True] * (PRIME_LEN + 1)
PRIMES = []
IS_PRIME[0] = False
IS_PRIME[1] = False
for i in range(2, PRIME_LEN + 1):
    if IS_PRIME[i]:
        PRIMES.append(i)
    j = 0
    while i * PRIMES[j] <= PRIME_LEN:
        IS_PRIME[i * PRIMES[j]] = False
        if i % PRIMES[j] == 0:
            break
        j += 1


class Solution:

    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        MAX = max(nums)
        uf = {}
        idxs = {}

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

        for i, v in enumerate(nums):
            if v in idxs:
                union(i, idxs[v])
            else:
                idxs[v] = i

        if 1 in idxs:
            return len(nums) == 1

        for PRIME in PRIMES:
            if PRIME > MAX:
                break
            founds = []
            for p in range(PRIME, MAX + 1, PRIME):
                if p in idxs:
                    founds.append(idxs[p])
            for i in range(1, len(founds)):
                union(founds[0], founds[i])

        return all(find(0) == find(i) for i in range(1, len(nums)))
