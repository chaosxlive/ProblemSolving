# https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for left in range(len(nums) - 2):
            if nums[left] == 0:
                continue
            right = left + 2
            for center in range(left + 1, len(nums) - 1):
                while right < len(nums) and nums[left] + nums[center] > nums[right]:
                    right += 1
                result += right - center - 1
        return result
