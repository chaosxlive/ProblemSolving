# https://leetcode.com/problems/valid-palindrome-iv/

class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        diffCnt = 0
        while left < right:
            if s[left] != s[right]:
                diffCnt += 1
            left += 1
            right -= 1
        return diffCnt < 3