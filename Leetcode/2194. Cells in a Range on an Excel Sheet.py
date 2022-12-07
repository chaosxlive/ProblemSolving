# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

from typing import List
from itertools import count, takewhile


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [f"{chr(ord(s[0]) + c)}{r}" for c in takewhile(lambda x:ord(s[0]) + x <= ord(s[3]), count(0)) for r in range(int(s[1]), int(s[4]) + 1)]
