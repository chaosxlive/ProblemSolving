# https://leetcode.com/problems/unique-number-of-occurrences/

from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence = defaultdict(lambda: 0)
        for num in arr:
            occurrence[num] += 1
        return len(occurrence) == len(set(occurrence.values()))
