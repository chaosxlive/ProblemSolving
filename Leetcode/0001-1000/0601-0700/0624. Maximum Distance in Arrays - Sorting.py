# https://leetcode.com/problems/maximum-distance-in-arrays/

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arr = sorted(item for items in map(lambda x: ((x[1][0], x[0]), (x[1][-1], x[0])), enumerate(arrays)) for item in items)
        if arr[0][1] == arr[-1][1]:
            return max(abs(arr[0][0] - arr[-2][0]), abs(arr[1][0] - arr[-1][0]))
        else:
            return abs(arr[0][0] - arr[-1][0])
