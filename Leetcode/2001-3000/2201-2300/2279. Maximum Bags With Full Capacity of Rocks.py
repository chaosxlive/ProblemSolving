# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

from typing import List
from itertools import accumulate, takewhile


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        return len(list(takewhile(lambda x: x <= additionalRocks, accumulate(candidate := sorted(filter(lambda x: x > 0, map(lambda x: x[0] - x[1], zip(capacity, rocks)))))))) + len(capacity) - len(candidate)
