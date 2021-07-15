# https://leetcode.com/contest/weekly-contest-248/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = nums[nums[i]]
        return result
