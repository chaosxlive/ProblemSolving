# https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        l = len(nums)
        result = 0
        for i in range(1, l + 1):
            subset = []
            for j in range(1, 101):
                p = i * j * j
                if p <= l:
                    subset.append(p)
                else:
                    break
            result = max(result, sum(map(lambda x: nums[x - 1], subset)))
        return result
