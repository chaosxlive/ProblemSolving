# https://leetcode.com/problems/partition-labels/

from typing import List
from collections import defaultdict


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = defaultdict(lambda: -1)
        for i, c in enumerate(s):
            lastSeen[c] = max(lastSeen[c], i)
        parts = [[0, 1]]
        for i, c in enumerate(s):
            if i == parts[-1][1]:
                parts.append([i, lastSeen[c] + 1])
            else:
                parts[-1][1] = max(parts[-1][1], lastSeen[c] + 1)
        return list(map(lambda x: x[1] - x[0], parts))
