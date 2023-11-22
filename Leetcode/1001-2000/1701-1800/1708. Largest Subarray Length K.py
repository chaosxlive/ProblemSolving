# https://leetcode.com/problems/largest-subarray-length-k/

from typing import List


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        idx = max((nums[i], i) for i in range(len(nums) - k + 1))[1]
        return nums[idx:idx + k]
