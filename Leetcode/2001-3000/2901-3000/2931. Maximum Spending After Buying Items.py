# https://leetcode.com/problems/maximum-spending-after-buying-items/

from typing import List
import heapq


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        h = [(vs.pop(), i) for i, vs in enumerate(values)]
        heapq.heapify(h)
        result = 0
        day = 1
        while len(h) > 0:
            v, i = heapq.heappop(h)
            result += v * day
            day += 1
            if len(values[i]) > 0:
                heapq.heappush(h, (values[i].pop(), i))
        return result
