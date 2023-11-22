# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = (1 + n) * n // 2
        divisibleCnt = n // m
        divisible = (m + m * divisibleCnt) * divisibleCnt // 2
        return total - 2 * divisible
