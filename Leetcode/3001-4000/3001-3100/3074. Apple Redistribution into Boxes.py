# https://leetcode.com/problems/apple-redistribution-into-boxes/

from typing import List


class Solution:

    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        cnt = sum(apple)
        i = 0
        while cnt > 0:
            cnt -= capacity[i]
            i += 1
        return i
