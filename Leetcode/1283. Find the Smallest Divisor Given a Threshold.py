# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        result = right
        while left <= right:
            mid = left + (right - left) // 2
            part = sum((n - 1) // mid + 1 for n in nums)
            if part > threshold:
                left = mid + 1
            else:
                result = min(result, mid)
                right = mid - 1
        return result