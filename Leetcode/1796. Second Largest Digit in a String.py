# https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution:
    def secondHighest(self, s: str) -> int:
        high1 = high2 = -1

        for c in s:
            if '0' <= c <= '9':
                temp = int(c)
                if temp > high1:
                    high2 = high1
                    high1 = temp
                elif temp < high1 and temp > high2:
                    high2 = temp
        return high2
