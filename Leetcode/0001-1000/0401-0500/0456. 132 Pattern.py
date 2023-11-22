# https://leetcode.com/problems/132-pattern/

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minN = 2147483647
        mins = [minN := min(minN, num) for num in nums]
        stack = []
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= mins[i]:
                continue
            while len(stack) > 0 and stack[-1] <= mins[i]:
                stack.pop()
            if len(stack) and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
        return False
