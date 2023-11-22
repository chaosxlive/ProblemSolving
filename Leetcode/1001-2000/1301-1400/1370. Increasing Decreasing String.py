# https://leetcode.com/problems/increasing-decreasing-string/

class Solution:
    def sortString(self, s: str) -> str:
        alphabet = [0] * 26
        for c in s:
            alphabet[ord(c) - 97] += 1

        result = ""
        length = len(s)
        rest = length
        while rest > 0:
            index = 0
            while index < 26:
                if alphabet[index] != 0:
                    result += chr(index + 97)
                    alphabet[index] -= 1
                    rest -= 1
                index += 1
            index = 25
            while index >= 0:
                if alphabet[index] != 0:
                    result += chr(index + 97)
                    alphabet[index] -= 1
                    rest -= 1
                index -= 1
        return result
