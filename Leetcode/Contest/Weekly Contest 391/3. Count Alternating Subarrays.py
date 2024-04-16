from typing import List, Optional


class Solution:

    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        result = 0
        prev = 0
        i = 1
        L = len(nums)
        while i < L:
            if nums[i] == nums[i - 1]:
                result += (1 + (i - prev)) * (i - prev) // 2
                prev = i
            i += 1
        result += (1 + (i - prev)) * (i - prev) // 2
        return result
