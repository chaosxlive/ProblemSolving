# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        fullWeek, rest = n // 7, n % 7
        # return (fullWeek - 1) * fullWeek // 2 * 7 + 28 * fullWeek + (2 * fullWeek + rest + 1) * rest // 2
        return (7 * fullWeek * fullWeek + 49 * fullWeek + 2 * fullWeek * rest + rest * rest + rest) // 2
