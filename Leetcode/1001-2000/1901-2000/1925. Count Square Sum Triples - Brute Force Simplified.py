# https://leetcode.com/problems/count-square-sum-triples/

from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a * a + b * b
                if c2 <= n * n and int(sqrt(c2)) ** 2 == c2:
                    result += 1
        return result
