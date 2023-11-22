# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower, upper = 1, n + 1
        while True:
            center = (lower + upper) // 2
            result = guess(center)
            if result < 0:
                upper = center
            elif result > 0:
                lower = center
            else:
                return center
