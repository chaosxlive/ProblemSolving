# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        prevChar = ''
        count = 0
        result = 0
        for c in s:
            if c != prevChar:
                if count > result:
                    result = count
                count = 0
                prevChar = c
            count += 1
        if count > result:
            result = count

        return result
            