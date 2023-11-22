# https://leetcode.com/problems/max-points-on-a-line/

from typing import List
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        slopes = defaultdict(set)
        for i in range(len(points) - 1):
            a, b = points[i]
            for j in range(i + 1, len(points)):
                c, d = points[j]
                if a == c:
                    slopes[(None, a)].add(i)
                    slopes[(None, a)].add(j)
                else:
                    alpha = (b - d) / (a - c)
                    beta = (a * d - b * c) / (a - c)
                    slopes[(alpha, beta)].add(i)
                    slopes[(alpha, beta)].add(j)
        return max(list(map(len, slopes.values())))
