# https://leetcode.com/problems/maximum-ice-cream-bars/

from typing import List
import heapq


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        picked = []
        for cost in costs:
            if len(picked) == 0:
                if cost <= coins:
                    picked.append(-cost)
                    coins -= cost
            else:
                if cost <= coins:
                    heapq.heappush(picked, -cost)
                    coins -= cost
                elif cost < -picked[0]:
                    coins += -heapq.heapreplace(picked, -cost) - cost
        return len(picked)
