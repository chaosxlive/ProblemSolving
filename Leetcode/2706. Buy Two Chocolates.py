# https://leetcode.com/problems/buy-two-chocolates/

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if prices[0] + prices[1] > money:
            return money
        return money - (prices[0] + prices[1])
