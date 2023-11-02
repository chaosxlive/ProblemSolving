# https://leetcode.com/problems/count-strictly-increasing-subarrays/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        stack = []
        result = 0
        for num in nums:
            if len(stack) > 0 and num <= stack[-1]:
                stack.clear()
            stack.append(num)
            result += len(stack)
        return result
