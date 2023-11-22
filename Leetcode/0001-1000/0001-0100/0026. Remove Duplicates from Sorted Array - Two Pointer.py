# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        index = 1
        for i in range(len(nums))[1:]:
            if nums[i] != nums[index - 1]:
                nums[index] = nums[i]
                index += 1
                
        return index
