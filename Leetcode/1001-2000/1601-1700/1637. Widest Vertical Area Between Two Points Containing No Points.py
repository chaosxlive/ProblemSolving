# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

from itertools import pairwise, starmap
from operator import sub
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return -min(starmap(sub, pairwise(sorted(x for x, _ in points))), default=0)
