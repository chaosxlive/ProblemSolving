# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            max1, max2 = nums[0], nums[1]
            i1 = 0
        else:
            max1, max2 = nums[1], nums[0]
            i1 = 1
        for i in range(2, len(nums)):
            if nums[i] >= max1:
                max1, max2 = nums[i], max1
                i1 = i
            elif nums[i] >= max2:
                max2 = nums[i]
        return i1 if max1 >= 2 * max2 else -1
