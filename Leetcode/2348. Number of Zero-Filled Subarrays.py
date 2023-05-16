# https://leetcode.com/problems/number-of-zero-filled-subarrays/

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        nums.append(1)
        cnt = 0
        for n in nums:
            if n == 0:
                cnt += 1
            else:
                result += (1 + cnt) * cnt // 2
                cnt = 0
        return result
