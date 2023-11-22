# https://leetcode.com/problems/total-cost-to-hire-k-workers/

import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        result = 0
        pickable = []
        left, right = candidates, len(costs) - candidates - 1
        if right < left:
            for i in range(len(costs)):
                heapq.heappush(pickable, (costs[i], i))
        else:
            for i in range(candidates):
                heapq.heappush(pickable, (costs[i], i))
            for i in range(len(costs) - candidates, len(costs)):
                heapq.heappush(pickable, (costs[i], i))
        for i in range(k):
            picked = heapq.heappop(pickable)
            result += picked[0]
            if right >= left:
                if picked[1] < left:
                    heapq.heappush(pickable, (costs[left], left))
                    left += 1
                else:
                    heapq.heappush(pickable, (costs[right], right))
                    right -= 1
        return result
