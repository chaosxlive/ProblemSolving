# https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        index = 0
        while index < len(s):
            if index % 2 == 0:
                result += s[index]
            else:
                result += self.shift(s[index - 1], int(s[index]))
            index += 1
        return result

    def shift(self, c, n):
        return chr((ord(c) - 97 + n) % 26 + 97)