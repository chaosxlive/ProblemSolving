# https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            current = nums[i]
            right -= current
            if left == right:
                return i
            left += current
        return -1
