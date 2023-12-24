# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        result = 2147483647
        stack = []
        for i in range(len(nums)):
            while len(stack) > 0 and nums[i] <= stack[-1]:
                if len(stack) >= 2 and stack[-1] > stack[0] and nums[i] < stack[-1]:
                    result = min(result, stack[0] + stack[-1] + nums[i])
                stack.pop()
            stack.append(nums[i])
        stack.clear()
        for i in reversed(range(len(nums))):
            while len(stack) > 0 and nums[i] <= stack[-1]:
                if len(stack) >= 2 and stack[-1] > stack[0] and nums[i] < stack[-1]:
                    result = min(result, stack[0] + stack[-1] + nums[i])
                stack.pop()
            stack.append(nums[i])
        return -1 if result == 2147483647 else result
