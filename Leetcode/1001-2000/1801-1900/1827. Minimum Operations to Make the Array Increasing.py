# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        prev = nums[0]
        for num in nums[1:]:
            if num <= prev:
                result += prev + 1 - num
                prev = prev + 1
            else:
                prev = num

        return result
