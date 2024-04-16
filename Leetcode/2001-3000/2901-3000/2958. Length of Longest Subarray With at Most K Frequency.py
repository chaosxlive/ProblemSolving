# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

from collections import defaultdict
from typing import List


class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = right = 0
        cnt = defaultdict(int)
        L = len(nums)
        result = 0
        while right < L:
            n = nums[right]
            cnt[n] += 1
            while cnt[n] > k:
                cnt[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result
