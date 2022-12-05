# https://leetcode.com/problems/palindrome-permutation/

from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        cnt1 = 0
        for f in c.values():
            if f % 2 == 1:
                cnt1 += 1
        return cnt1 <= 1
