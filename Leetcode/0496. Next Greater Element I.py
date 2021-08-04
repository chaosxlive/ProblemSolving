# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) and nums2[i] > stack[-1]:
                stack.pop()
            if len(stack) == 0:
                nextGreater[nums2[i]] = -1
            else:
                nextGreater[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        return [nextGreater[nums1[i]] for i in range(len(nums1))]
