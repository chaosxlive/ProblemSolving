# https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        bias = 0
        while True:
            if start - bias >= 0 and nums[start - bias] == target:
                return bias
            if start + bias < len(nums) and nums[start + bias] == target:
                return bias
            bias += 1
