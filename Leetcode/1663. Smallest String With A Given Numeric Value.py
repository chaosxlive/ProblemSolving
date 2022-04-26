# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

from string import ascii_lowercase


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = []
        k -= n
        while k:
            if k >= 25:
                result.append('z')
                k -= 25
            else:
                result.append(ascii_lowercase[k])
                k = 0
        while len(result) < n:
            result.append('a')
        return ''.join(result[::-1])
