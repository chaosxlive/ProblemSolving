# https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result = 0
        patch = 0
        index = 0
        while patch < n:
            if index < len(nums) and patch + 1 >= nums[index]:
                patch += nums[index]
                index += 1
            else:
                patch += patch + 1
                result += 1
        return result
