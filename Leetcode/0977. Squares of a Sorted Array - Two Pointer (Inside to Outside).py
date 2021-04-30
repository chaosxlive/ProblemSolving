# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = 0
        while right + 1 < len(nums):
            if abs(nums[right]) < abs(nums[right + 1]):
                break
            right += 1
        left = right - 1

        result = []
        while left >= 0 and right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[left] * nums[left])
                left -= 1
            else:
                result.append(nums[right] * nums[right])
                right += 1

        while left >= 0:
            result.append(nums[left] * nums[left])
            left -= 1
        while right < len(nums):
            result.append(nums[right] * nums[right])
            right += 1

        return result