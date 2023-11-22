# https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 0
        prevChar = ''
        count = 0
        for c in s:
            if c != prevChar:
                result += (1 + count) * count // 2
                count = 0
                prevChar = c
            count += 1
        result += (1 + count) * count // 2

        return result % 1000000007