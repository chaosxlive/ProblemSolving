import heapq
from typing import List, Optional


class Solution:

    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        h = [(v, i) for i, v in enumerate(nums)]
        S = sum(nums)
        heapq.heapify(h)
        marked = set()
        result = []
        for i, k in queries:
            if i not in marked:
                marked.add(i)
                S -= nums[i]
            for i in range(k):
                while len(h) > 0:
                    mv, mi = heapq.heappop(h)
                    if mi not in marked:
                        marked.add(mi)
                        S -= mv
                        break
            result.append(S)
        return result
