# https://leetcode.com/problems/binary-trees-with-factors/

from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = [1] * len(arr)
        idxs = {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    k = x / arr[j]
                    if k in idxs:
                        dp[i] += dp[j] * dp[idxs[k]]
                        dp[i] %= 1000000007
        return sum(dp) % 1000000007
