# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

from typing import List
import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        h = list(map(lambda x: (x[1], x[0]), enumerate(nums)))
        heapq.heapify(h)
        marks = [False] * len(nums)
        result = 0
        while len(h) > 0:
            n, i = heapq.heappop(h)
            if marks[i]:
                continue
            result += n
            marks[i] = True
            if i > 0:
                marks[i - 1] = True
            if i + 1 < len(nums):
                marks[i + 1] = True
        return result
