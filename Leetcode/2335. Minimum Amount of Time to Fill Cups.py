# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        result = 0
        while True:
            amount.sort(reverse=True)
            if amount[2] == 0:
                break
            amount[0] -= 1
            amount[1] -= 1
            result += 1
        result += max(amount[0], amount[1])
        return result
