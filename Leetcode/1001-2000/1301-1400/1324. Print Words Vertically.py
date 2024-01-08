# https://leetcode.com/problems/print-words-vertically/

from itertools import starmap
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        p = s.split(' ')
        L = max(map(len, p))
        return list(starmap(lambda *x: ''.join(x).rstrip(' '), zip(*list(map(lambda w: list(w.ljust(L)), p)))))
