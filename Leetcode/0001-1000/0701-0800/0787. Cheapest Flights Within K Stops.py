# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for step in range(k + 1):
            newPrices = prices[:]
            for fFrom, fTo, fPrice in flights:
                if prices[fFrom] == float('inf'):
                    continue
                newPrices[fTo] = min(newPrices[fTo], prices[fFrom] + fPrice)
            prices = newPrices
        return -1 if prices[dst] == float('inf') else prices[dst]
