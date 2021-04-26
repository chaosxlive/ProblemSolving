# https://leetcode.com/problems/furthest-building-you-can-reach/
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        difSum = 0
        for index in range(len(heights) - 1):
            dif = heights[index + 1] - heights[index]
            if dif > 0:
                heapq.heappush(heap, dif)
                if len(heap) > ladders:
                    difSum += heapq.heappop(heap)

                if difSum > bricks:
                    return index
        return len(heights) - 1
