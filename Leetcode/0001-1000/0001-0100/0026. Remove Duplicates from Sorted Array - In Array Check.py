# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        index = 0
        for i in range(len(nums)):
            if nums[i] not in nums[0: index]:
                nums[index] = nums[i]
                index += 1
        
        return index