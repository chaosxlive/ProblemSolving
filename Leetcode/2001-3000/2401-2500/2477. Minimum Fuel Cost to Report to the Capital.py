# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

from typing import List
from collections import defaultdict
from math import ceil


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        neighbors = defaultdict(list)
        for x, y in roads:
            neighbors[x].append(y)
            neighbors[y].append(x)
        self.result = 0

        def dfs(city, prev, people=1):
            for x in neighbors[city]:
                if x == prev:
                    continue
                people += dfs(x, city)
            self.result += int(ceil(people / seats)) if city else 0
            return people

        dfs(0, 0)
        return self.result
