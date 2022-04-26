# https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution:
    def minimumMoves(self, s: str) -> int:
        result = index = 0
        while index < len(s):
            if s[index] == 'X':
                result += 1
                index += 3
            else:
                index += 1
        return result
