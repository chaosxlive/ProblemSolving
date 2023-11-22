# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptrRead = ptrWrite = 0

        while ptrRead < len(nums):
            if nums[ptrRead] == 0:
                ptrRead += 1
                continue
            nums[ptrWrite] = nums[ptrRead]
            ptrRead += 1
            ptrWrite += 1
        
        while ptrWrite < len(nums):
            nums[ptrWrite] = 0
            ptrWrite += 1