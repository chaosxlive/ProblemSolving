# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        result = 0
        for num in left:
            result = max(result, num)
        for num in right:
            result = max(result, n - num)
        return result
