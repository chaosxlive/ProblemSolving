# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List
from collections import deque


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        result = 0
        last7 = deque()
        last30 = deque()
        for day in days:
            while last7 and last7[0][0] + 7 <= day:
                last7.popleft()
            while last30 and last30[0][0] + 30 <= day:
                last30.popleft()
            last7.append((day, result + costs[1]))
            last30.append((day, result + costs[2]))
            result = min(result + costs[0], last7[0][1], last30[0][1])
        return result
