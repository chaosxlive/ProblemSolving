# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

from collections import defaultdict
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = defaultdict(lambda: 0)
        for card in deck:
            counts[card] += 1
        counts = list(counts.values())
        prev = counts[0]
        for i in range(1, len(counts)):
            prev = gcd(prev, counts[i])
            if prev < 2:
                return False
        return prev >= 2