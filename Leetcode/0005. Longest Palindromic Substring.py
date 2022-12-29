# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # https://medium.com/hoskiss-stand/manacher-299cf75db97e
        sLen = len(s)
        if sLen < 3:
            if s == s[::-1]:
                return s
            return s[0]

        sFixed = ''.join(['#'] + [c + '#' for c in s])
        sFixedLen = len(sFixed)
        lps = [0] * sFixedLen

        mid = 1
        rightMax = 2
        lenMax = 0
        lpsMid = 0

        for i in range(1, sFixedLen):
            lps[i] = min(lps[mid * 2 - i], rightMax - i) if i < rightMax else 0

            while (
                i - lps[i] - 1 >= 0 and
                i + lps[i] + 1 < sFixedLen and
                sFixed[i - lps[i] - 1] == sFixed[i + lps[i] + 1]
            ):
                lps[i] += 1

            if lps[i] > lenMax:
                lenMax = lps[i]
                lpsMid = i

            if lps[i] + i - 1 > rightMax:
                rightMax = lps[i] + i - 1
                mid = i

        left = (lpsMid - lenMax) // 2
        return s[left: left + lenMax]
