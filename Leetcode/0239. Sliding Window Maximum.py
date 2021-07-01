# https://leetcode.com/problems/sliding-window-maximum/

import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowHeap = [(-val, index) for index, val in enumerate(nums[:k - 1])]
        heapq.heapify(windowHeap)
        result = []
        for i in range(k - 1, len(nums)):
            heapq.heappush(windowHeap, (-nums[i], i))
            while windowHeap[0][1] <= i - k:
                heapq.heappop(windowHeap)
            result.append(-windowHeap[0][0])
        return result
