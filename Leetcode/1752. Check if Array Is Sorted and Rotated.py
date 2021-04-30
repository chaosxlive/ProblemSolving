# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        isRotated = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if not isRotated:
                    isRotated = True
                else:
                    return False
        
        if isRotated and nums[len(nums) - 1] > nums[0]:
            return False
        return True