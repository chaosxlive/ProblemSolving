# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            center = (left + right) // 2
            if nums[center] == target:
                return center
            if nums[center] > target:
                right = center
            else:
                left = center + 1
        if left == len(nums) or nums[left] >= target:
            return left
        return left + 1
