# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/submissions/

import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1
        lower, upper = 1, 1000000001
        result = 1000000001
        while True:
            count = 0
            center = (lower + upper) // 2
            for i in range(len(dist) - 1):
                count += math.ceil(dist[i] / center)
            count += dist[-1] / center
            if count <= hour:
                if center < result:
                    result = center
                upper = center
            else:
                lower = center + 1
            if lower >= upper:
                return result