# https://leetcode.com/problems/avoid-flood-in-the-city/

from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        days = []
        lastFull = defaultdict(lambda: -1)
        result = [-1] * len(rains)
        for d, lake in enumerate(rains):
            if lake > 0:
                if lastFull[lake] > -1:
                    if len(days) == 0:
                        return []
                    idx = bisect_left(days, lastFull[lake])
                    if idx >= len(days):
                        return []
                    result[days[idx]] = lake
                    del days[idx]
                lastFull[lake] = d
            else:
                days.append(d)
        for day in days:
            result[day] = 1
        return result
