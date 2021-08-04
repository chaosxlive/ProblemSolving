# https://leetcode.com/contest/biweekly-contest-57/problems/check-if-all-characters-have-equal-number-of-occurrences

from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = list(Counter(s).items())

        for c, i in count[1:]:
            if i != count[0][1]:
                return False
        return True
