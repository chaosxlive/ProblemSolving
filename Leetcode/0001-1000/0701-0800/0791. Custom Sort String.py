# https://leetcode.com/problems/custom-sort-string/

from collections import defaultdict


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        charIndex = defaultdict(int)
        for i in range(len(order)):
            charIndex[order[i]] = i
        
        return "".join(sorted(list(str), key=lambda x: charIndex[x]))
