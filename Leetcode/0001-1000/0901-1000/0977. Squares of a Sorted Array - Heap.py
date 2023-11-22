# https://leetcode.com/problems/squares-of-a-sorted-array/
import heapq

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, abs(num))
        
        result = []
        for i in range(len(heap)):
            temp = heapq.heappop(heap)
            result.append(temp * temp)
        
        return result