# https://leetcode.com/problems/h-index/

from collections import Counter


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = sorted(Counter(citations).items(), reverse=True)
        countSum = 0
        index = 0
        h = len(citations)
        while True:
            while index < len(counts) and counts[index][0] >= h:
                countSum += counts[index][1]
                index += 1
            if countSum >= h:
                return h
            h -= 1
