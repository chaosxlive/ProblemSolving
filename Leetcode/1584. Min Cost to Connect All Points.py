# https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)]
        isInMST = [False] * len(points)
        cost = 0
        edgeUsedCount = 0

        while edgeUsedCount < len(points):
            weight, currentIndex = heapq.heappop(heap)

            if isInMST[currentIndex]:
                continue

            isInMST[currentIndex] = True
            edgeUsedCount += 1
            cost += weight

            for nextIndex in range(len(points)):
                if not isInMST[nextIndex]:
                    nextWeight = abs(points[currentIndex][0] - points[nextIndex][0]) + abs(points[currentIndex][1] - points[nextIndex][1])
                    heapq.heappush(heap, (nextWeight, nextIndex))

        return cost
