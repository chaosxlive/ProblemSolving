# https://leetcode.com/problems/ipo/

from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        candidates = []
        money = w
        thresholds = sorted(zip(capital, profits))
        idx = 0
        for i in range(k):
            while idx < len(thresholds) and thresholds[idx][0] <= money:
                heapq.heappush(candidates, -thresholds[idx][1])
                idx += 1
            if len(candidates) > 0:
                money += -heapq.heappop(candidates)
        return money
