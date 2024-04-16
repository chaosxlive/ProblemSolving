# https://leetcode.com/problems/subarrays-with-k-different-integers/

from typing import List


class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnts = [0] * (len(nums) + 1)
        res = 0
        left = right = 0
        for n in nums:
            cnts[n] += 1
            if cnts[n] == 1:
                k -= 1
                if k < 0:
                    cnts[nums[right]] = 0
                    right += 1
                    left = right
            if k <= 0:
                while cnts[nums[right]] > 1:
                    cnts[nums[right]] -= 1
                    right += 1
                res += right - left + 1
        return res
