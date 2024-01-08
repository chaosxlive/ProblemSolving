# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devs = list(filter(None, map(lambda b: b.count('1'), bank)))
        return sum(a*b for a, b in zip(devs, devs[1:]))
