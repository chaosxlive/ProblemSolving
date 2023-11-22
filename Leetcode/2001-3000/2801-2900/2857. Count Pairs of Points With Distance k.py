# https://leetcode.com/problems/count-pairs-of-points-with-distance-k/description/

from typing import List
from collections import Counter


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        counter = Counter(map(tuple, coordinates))
        result = 0
        if k == 0:
            for p in counter.keys():
                result += counter[tuple(p)] * (counter[tuple(p)] - 1) // 2
            return result
        for i in range(k + 1):
            for p in coordinates:
                result += counter[(p[0] ^ i, p[1] ^ (k - i))]
        return result // 2
