# https://leetcode.com/problems/koko-eating-bananas/

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left <= right:
            mid = left + (right - left) // 2
            time = sum((p - 1) // mid + 1 for p in piles)
            if time > h:
                left = mid + 1
            else:
                result = min(result, mid)
                right = mid - 1
        return result
