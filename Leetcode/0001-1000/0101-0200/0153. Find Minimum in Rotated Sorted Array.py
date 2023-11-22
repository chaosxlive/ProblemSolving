# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            center = (left + right) // 2

            if nums[center] > nums[center + 1]:
                return nums[center + 1]

            if nums[center - 1] > nums[center]:
                return nums[center]

            if nums[center] > nums[0]:
                left = center + 1
            else:
                right = center - 1
