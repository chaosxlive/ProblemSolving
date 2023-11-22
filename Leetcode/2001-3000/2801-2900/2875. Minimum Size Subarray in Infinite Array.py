# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

from typing import List
from itertools import accumulate


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        prefix = [0] + list(accumulate(nums + nums))
        result = 2147483647
        resultFull = 0
        if target == total:
            return len(nums)
        resultFull = len(nums) * (target // total)
        target %= total
        left, right = 0, 1
        while right < len(prefix):
            if prefix[right] - prefix[left] > target:
                left += 1
            elif prefix[right] - prefix[left] < target:
                right += 1
            else:
                result = min(result, right - left)
                left += 1
                right += 1

        return result + resultFull if result != 2147483647 else -1
