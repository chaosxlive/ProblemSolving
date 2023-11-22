# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        index = 1
        while index < len(nums):
            if nums[index] < nums[index - 1]:
                if index >= 2:
                    temp = nums[index - 1]
                    nums[index - 1] = nums[index - 2]
                    if self.checkModified(nums, index - 1):
                        return True
                    nums[index - 1] = temp
                else:
                    temp = nums[index - 1]
                    nums[index - 1] = nums[index]
                    if self.checkModified(nums, index - 1):
                        return True
                    nums[index - 1] = temp
                nums[index] = nums[index - 1]
                return self.checkModified(nums, index)
            index += 1
        return True

    def checkModified(self, nums, index) -> bool:
        for i in range(max(1, index - 2), len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True
