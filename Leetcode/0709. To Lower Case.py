# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ""
        for c in str:
            result += chr(ord(c) + 32) if 'A' <= c <= 'Z' else c
        return result
