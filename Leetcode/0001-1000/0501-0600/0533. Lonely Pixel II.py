# https://leetcode.com/problems/lonely-pixel-ii/

from collections import defaultdict
from typing import List


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        rs = defaultdict(int)
        cs = defaultdict(int)

        def m(ss: List[str]) -> int:
            return int(''.join('1' if s == 'B' else '0' for s in ss), 2)

        rm = [m(r) for r in picture]

        for r, R in enumerate(picture):
            for c, C in enumerate(R):
                if C == 'B':
                    rs[r] += 1
                    cs[c] += 1

        result = 0
        for r, R in enumerate(picture):
            for c, C in enumerate(R):
                if C == 'B' and rs[r] == target and cs[c] == target:
                    s = rm[r]
                    isValid = True
                    for ri, rr in enumerate(picture):
                        if rr[c] == 'B' and s != rm[ri]:
                            isValid = False
                            break
                    if isValid:
                        result += cs[c]
                    cs[c] = -1
        return result
