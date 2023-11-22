# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-2147483649)

        left, right = 0, len(nums)
        while True:
            center = (left + right) // 2
            if nums[center - 1] > nums[center]:
                right = center
            elif nums[center + 1] > nums[center]:
                left = center + 1
            else:
                return center
