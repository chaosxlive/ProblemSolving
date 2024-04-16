# https://leetcode.com/problems/find-the-index-of-permutation/

from typing import List
from sortedcontainers import SortedList

MOD = 10**9 + 7
FACT = [1] * (10**5 + 1)
for i in range(2, len(FACT)):
    FACT[i] = (FACT[i - 1] * i) % MOD


class Solution:

    def getPermutationIndex(self, perm: List[int]) -> int:
        ns = SortedList(perm)
        res = 0
        for n in perm:
            i = ns.bisect_left(n)
            res += i * FACT[len(ns) - 1]
            res %= MOD
            ns.pop(i)
        return res
