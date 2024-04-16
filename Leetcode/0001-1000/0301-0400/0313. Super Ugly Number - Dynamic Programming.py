# https://leetcode.com/problems/super-ugly-number/

import heapq
from typing import List


class Solution:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglyNums = [0] * n
        idxs = [0] * len(primes)
        nexts = [(1, i) for i in range(len(primes))]
        for i in range(n):
            uglyNums[i] = nexts[0][0]
            while nexts[0][0] == uglyNums[i]:
                _, nextI = heapq.heappop(nexts)
                heapq.heappush(nexts, (uglyNums[idxs[nextI]] * primes[nextI], nextI))
                idxs[nextI] += 1
        return uglyNums[-1]
