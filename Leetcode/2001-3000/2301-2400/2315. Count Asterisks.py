# https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        result = 0
        isCount = True
        for c in s:
            if c == '|':
                isCount = not isCount
            elif isCount and c == '*':
                result += 1
        return result
