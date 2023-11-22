# https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = sorted(Counter(arr).values(), reverse=True)
        countSum = 0
        for i in range(len(count)):
            countSum += count[i]
            if countSum * 2 >= len(arr):
                return i + 1
        return len(count)
