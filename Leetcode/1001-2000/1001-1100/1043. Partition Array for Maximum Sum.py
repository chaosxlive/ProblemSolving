# https://leetcode.com/problems/partition-array-for-maximum-sum/

from typing import List


class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        L = len(arr)
        cached = [-1] * (L + 1)

        def solve(idx: int):
            if idx >= L:
                return 0
            if cached[idx] != -1:
                return cached[idx]
            currMax = 0
            result = 0
            for i in range(idx, min(L, idx + k)):
                currMax = max(currMax, arr[i])
                result = max(result, currMax * (i - idx + 1) + solve(i + 1))
            cached[idx] = result
            return result

        return solve(0)
