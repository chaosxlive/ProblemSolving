# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        zeroCount = result = 0
        while right < len(nums):
            if nums[right] == 0:
                zeroCount += 1
                while zeroCount > k:
                    if nums[left] == 0:
                        zeroCount -= 1
                    left += 1
            result = max(result, right - left + 1)
            right += 1
        return result
