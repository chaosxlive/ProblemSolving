from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List, Optional


class Solution:

    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        neighbors = defaultdict(list)
        times = {}
        for a, b, t in edges:
            if a == b:
                continue
            neighbors[a].append(b)
            neighbors[b].append(a)
            if (min(a, b), max(a, b)) in times:
                times[(min(a, b), max(a, b))] = min(times[(min(a, b), max(a, b))], t)
            else:
                times[(min(a, b), max(a, b))] = t
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


# print(Solution().)
