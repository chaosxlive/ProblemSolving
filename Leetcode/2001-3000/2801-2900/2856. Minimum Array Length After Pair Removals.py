# https://leetcode.com/problems/minimum-array-length-after-pair-removals/

from typing import List
import heapq
from collections import Counter


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        c = Counter(nums)
        h = list(map(lambda x: -x, c.values()))
        heapq.heapify(h)

        while len(h) > 1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)
            a -= 1
            b -= 1
            if a > 0:
                heapq.heappush(h, -a)
            if b > 0:
                heapq.heappush(h, -b)

        if len(h) == 0:
            return 0
        return -h[0]
