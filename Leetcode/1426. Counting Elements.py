# https://leetcode.com/problems/counting-elements/

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        result = 0
        for n in arr:
            if n + 1 in seen:
                result += 1
        return result
