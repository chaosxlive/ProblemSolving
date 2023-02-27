# https://leetcode.com/problems/minimize-deviation-in-array/

from typing import List
import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = list(map(lambda n: -n if n % 2 == 0 else -n * 2, nums))
        minNum = -max(heap)
        heapq.heapify(heap)
        result = 2147483647
        while heap[0] % 2 == 0:
            num = -heapq.heapreplace(heap, heap[0] // 2)
            result = min(result, num - minNum)
            minNum = min(minNum, num // 2)
        return min(result, -heap[0] - minNum)
