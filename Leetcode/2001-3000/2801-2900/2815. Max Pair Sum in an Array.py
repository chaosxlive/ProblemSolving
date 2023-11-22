# https://leetcode.com/problems/max-pair-sum-in-an-array/

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        buckets = {i: [] for i in range(0, 10)}
        for num in nums:
            _num = num
            maxD = 0
            while num > 0:
                maxD = max(maxD, num % 10)
                num //= 10
            buckets[maxD].append(_num)
        vs = list(sum(sorted(bucket, reverse=True)[:2]) for bucket in buckets.values() if len(bucket) > 1)
        if len(vs) == 0:
            return -1
        return max(vs)
