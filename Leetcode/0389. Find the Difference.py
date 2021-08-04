# https://leetcode.com/problems/find-the-difference/

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        countS, countT = Counter(s), Counter(t)
        for c in "abcdefghijklmnopqrstuvwxyz":
            diff = abs(countS[c] - countT[c])
            if diff > 0:
                return c
