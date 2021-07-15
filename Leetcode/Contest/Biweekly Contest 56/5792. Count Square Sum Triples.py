# https://leetcode.com/contest/biweekly-contest-56/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                for c in range(1, n + 1):
                    if a ** 2 + b ** 2 == c ** 2:
                        result += 1
        return result

# TLE