# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from typing import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stones = list(map(lambda x: -x, piles))
        heapq.heapify(stones)
        for i in range(k):
            stone = -heapq.heappop(stones)
            heapq.heappush(stones, -((stone + 1) // 2))
        return -sum(stones)
