# https://leetcode.com/problems/number-of-valid-subarrays/

from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        result = 0
        for v in nums:
            while len(stack) > 0 and v < stack[-1]:
                stack.pop()
            stack.append(v)
            result += len(stack)
        return result
