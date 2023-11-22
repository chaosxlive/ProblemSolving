# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

from typing import List
import heapq
from bisect import bisect_left
from collections import Counter


class Solution:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        thresholds = {(0, 0): grid[0][0]}
        # BFS base on lower threshold
        heap = [(grid[0][0], 0, 0)]
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while len(heap) > 0:
            threshold, row, col = heapq.heappop(heap)
            for dr, dc in dirs:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and (row + dr, col + dc) not in thresholds:
                    newThreshold = max(threshold, grid[row + dr][col + dc])
                    thresholds[(row + dr, col + dc)] = newThreshold
                    heapq.heappush(heap, (newThreshold, row + dr, col + dc))
        counter = Counter(thresholds.values())
        thresholdKeys = [0] + sorted(set(thresholds.values()))
        prefixSum = [counter[n] for n in thresholdKeys]
        for i in range(1, len(prefixSum)):
            prefixSum[i] += prefixSum[i - 1]
        return [prefixSum[bisect_left(thresholdKeys, q) - 1] for q in queries]
