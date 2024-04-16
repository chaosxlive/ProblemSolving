# https://leetcode.com/problems/super-ugly-number/

import heapq
from typing import List


class Solution:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        h = [1]
        seen = set()
        while True:
            num = heapq.heappop(h)
            if n == 1:
                return num
            n -= 1
            for p in primes:
                m = num * p
                if m not in seen:
                    heapq.heappush(h, m)
                    seen.add(m)
