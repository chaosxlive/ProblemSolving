# https://leetcode.com/problems/jump-game-vi/

import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        for index in range(1, len(nums)):
            while heap[0][1] < index - k:
                heapq.heappop(heap)
            if index == len(nums) - 1:
                return -heap[0][0] + nums[index]
            heapq.heappush(heap, (heap[0][0] - nums[index], index))
        return nums[0]
