# https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

from collections import defaultdict
from math import inf
from typing import List


class Solution:

    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        L = len(nums)
        total = (1 + L) * L // 2
        medIdx = (total - 1) // 2
        result = inf

        left, right = 0, len(set(nums))
        while left <= right:
            mid = left + (right - left) // 2
            freqs = defaultdict(int)
            cnt = 0
            j = 0
            res = 0
            for i, n in enumerate(nums):
                if freqs[n] == 0:
                    cnt += 1
                freqs[n] += 1
                while cnt > mid:
                    freqs[nums[j]] -= 1
                    if freqs[nums[j]] == 0:
                        cnt -= 1
                    j += 1
                res += i - j + 1
            if res - 1 >= medIdx:
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid + 1
        return result
