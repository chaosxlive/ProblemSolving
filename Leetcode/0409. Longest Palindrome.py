# https://leetcode.com/problems/longest-palindrome/

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        hasSingle = False
        for c in count.values():
            if c % 2 == 1:
                hasSingle = True
            result += (c // 2) * 2
        return result + 1 if hasSingle else result
