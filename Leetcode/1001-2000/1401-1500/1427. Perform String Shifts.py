# https://leetcode.com/problems/perform-string-shifts/

from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final = 0
        for d, n in shift:
            if d == 0:
                final -= n
            else:
                final += n
        final %= len(s)
        return (s + s)[len(s) - final:len(s) * 2 - final]
