# https://leetcode.com/problems/missing-number-in-arithmetic-progression/

from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[0] == arr[1]:
            return arr[0]
        diff = (arr[-1] - arr[0]) // len(arr)
        idx = 0
        while True:
            if arr[idx + 1] != arr[idx] + diff:
                return arr[idx] + diff
            idx += 1
