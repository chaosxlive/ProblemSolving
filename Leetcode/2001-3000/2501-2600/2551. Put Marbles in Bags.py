# https://leetcode.com/problems/put-marbles-in-bags/

from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = sorted(sum(w) for w in zip(weights, weights[1:]))
        return sum(pairs[-1:-k:-1]) - sum(pairs[:k - 1])
        
