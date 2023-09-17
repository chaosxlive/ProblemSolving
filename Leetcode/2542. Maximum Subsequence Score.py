# https://leetcode.com/problems/maximum-subsequence-score/

from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums2, nums1), reverse=True)

        min2 = min(map(lambda x: x[0], nums[:k]))
        h = list(map(lambda x: x[1], nums[:k]))
        sum1 = sum(h)
        result = min2 * sum1
        heapq.heapify(h)

        for i in range(k, len(nums)):
            if nums[i][1] < h[0]:
                continue
            min2 = min(min2, nums[i][0])
            p = heapq.heapreplace(h, nums[i][1])
            sum1 += nums[i][1] - p
            result = max(result, min2 * sum1)
        return result
