# https://leetcode.com/problems/maximum-performance-of-a-team/

import heapq


class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        engineers = sorted(zip(efficiency, speed), key=lambda x: x[0], reverse=True)

        heap = []
        speedSum = result = 0
        for currentEff, currentSpeed in engineers:
            if len(heap) == k:
                speedSum -= heapq.heappop(heap)
            speedSum += currentSpeed
            heapq.heappush(heap, currentSpeed)
            result = max(result, speedSum * currentEff)
        return result % 1000000007
