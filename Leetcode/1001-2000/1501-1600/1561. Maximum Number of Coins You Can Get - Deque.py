# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from collections import deque
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        dq = deque(sorted(piles))
        result = 0
        while len(dq) > 0:
            dq.pop()
            dq.popleft()
            result += dq.pop()
        return result
