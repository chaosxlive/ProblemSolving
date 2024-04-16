import heapq
from typing import List, Optional


class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        cnt = 0
        while nums[0] < k:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            heapq.heappush(nums, min(a, b) * 2 + max(a, b))
            cnt += 1
        return cnt
