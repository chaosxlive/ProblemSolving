# https://leetcode.com/problems/maximum-number-of-alloys/

from typing import List


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        result = 0
        for m in composition:
            left = 0
            right = 2147483647
            while left <= right:
                mid = left + (right - left) // 2
                c = sum(cost[i] * max(0, mid * m[i] - stock[i]) for i in range(n))
                if c <= budget:
                    result = max(result, mid)
                    left = mid + 1
                else:
                    right = mid - 1
        return result
