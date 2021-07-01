# https://leetcode.com/contest/biweekly-contest-55/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        def checkIgnore(nums):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return checkIgnore(nums[:i - 1] + nums[i:]) or checkIgnore(nums[:i] + nums[i + 1:])
        return True
