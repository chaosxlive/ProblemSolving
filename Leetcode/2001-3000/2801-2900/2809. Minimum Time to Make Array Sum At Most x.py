# https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        arr = sorted([(nums2[i], nums1[i]) for i in range(n)])
        dp = [0] * (n + 1)
        for n2, n1 in arr:
            for i in range(n-1, -1, -1):
                dp[i + 1] = max(dp[i + 1], dp[i] + (i + 1) * n2 + n1)
        s2 = sum(nums2)
        s1 = sum(nums1)
        for i in range(n + 1):
            if s2 * i + s1 - dp[i] <= x:
                return i
        return -1
