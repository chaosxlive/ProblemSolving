# https://leetcode.com/problems/lonely-pixel-i/

from collections import defaultdict
from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rs = defaultdict(int)
        cs = defaultdict(int)
        for r, R in enumerate(picture):
            for c, C in enumerate(R):
                if C == 'B':
                    rs[r] += 1
                    cs[c] += 1
        return sum(1 for r, R in enumerate(picture) for c, C in enumerate(R) if C == 'B' and rs[r] == 1 and cs[c] == 1)
