# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def isAlphanumeric(c):
            return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'

        def toLower(c):
            return chr(ord(c) + 32) if 'A' <= c <= 'Z' else c

        while True:
            while left < len(s) and not isAlphanumeric(s[left]):
                left += 1
            while right >= 0 and not isAlphanumeric(s[right]):
                right -= 1
            if left < len(s) and right >= 0 and toLower(s[left]) != toLower(s[right]):
                return False
            if left >= right:
                return True
            left += 1
            right -= 1
