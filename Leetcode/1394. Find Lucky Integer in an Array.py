# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = [num for num, freq in Counter(arr).items() if num == freq]
        return -1 if len(result) == 0 else max(result)
