# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        s = 0
        n = 0
        for w in weight:
            if s + w > 5000:
                break
            s += w
            n += 1
        return n
