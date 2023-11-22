# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) and nums[i] >= stack[-1]:
                stack.pop()
            stack.append(nums[i])

        result = [-1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) and nums[i] >= stack[-1]:
                stack.pop()
            if len(stack) == 0:
                result[i] = -1
            else:
                result[i] = stack[-1]
            stack.append(nums[i])
        return result
