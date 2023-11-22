# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        result = [0] * len(nums)
        index = 0
        for num in nums:
            if num != 0:
                result[index] = num
                index += 1
        return result
