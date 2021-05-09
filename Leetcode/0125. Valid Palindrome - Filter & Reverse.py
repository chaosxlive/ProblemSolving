# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = filter(lambda x: 'a' <= x <= 'z' or 'A' <= x <= 'Z' or '0' <= x <= '9', s)
        filtered = "".join(list(chars)).lower()
        return filtered == filtered[::-1]
