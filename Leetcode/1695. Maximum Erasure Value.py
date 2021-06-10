# https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = right = result = currentSum = 0
        seen = set()
        while right < len(nums):
            if nums[right] not in seen:
                currentSum += nums[right]
                if currentSum > result:
                    result = currentSum
                seen.add(nums[right])
                right += 1
            else:
                while left < right:
                    if nums[left] == nums[right]:
                        left += 1
                        right += 1
                        break
                    currentSum -= nums[left]
                    seen.remove(nums[left])
                    left += 1
        return result
