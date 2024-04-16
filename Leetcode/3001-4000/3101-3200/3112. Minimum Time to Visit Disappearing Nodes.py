# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:

    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        neighbors = defaultdict(list)
        times = defaultdict(lambda: inf)
        for a, b, t in edges:
            if a == b:
                continue
            neighbors[a].append(b)
            neighbors[b].append(a)
            times[(min(a, b), max(a, b))] = min(times[(min(a, b), max(a, b))], t)
        res = [-1] * n
        q = [(0, 0)]
        while len(q) > 0:
            time, node = heappop(q)
            if res[node] > -1:
                continue
            if time >= disappear[node]:
                continue
            res[node] = time
            for neighbor in neighbors[node]:
                if res[neighbor] > -1:
                    continue
                heappush(q, (time + times[min(node, neighbor), max(node, neighbor)], neighbor))
        return res
