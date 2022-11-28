# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            center = (left + right) // 2
            if (center % 2 == 1 and nums[center - 1] == nums[center]) or (center % 2 == 0 and nums[center] == nums[center + 1]):
                left = center + 1
            else:
                right = center
        return nums[left]
