# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result += [nums[left] * nums[left]]
                left += 1
            else:
                result += [nums[right] * nums[right]]
                right -= 1
        return result[::-1]