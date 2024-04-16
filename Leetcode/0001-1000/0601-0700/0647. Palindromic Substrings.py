# https://leetcode.com/problems/palindromic-substrings/


class Solution:

    def countSubstrings(self, s: str) -> int:
        L = len(s)
        result = L
        for center in range(L):
            l = 1
            while 0 <= center - l and center + l < L and s[center - l] == s[center + l]:
                result += 1
                l += 1
            if center == L - 1:
                continue
            l = 1
            while 0 <= center - l + 1 and center + l < L and s[center - l + 1] == s[center + l]:
                result += 1
                l += 1
        return result
