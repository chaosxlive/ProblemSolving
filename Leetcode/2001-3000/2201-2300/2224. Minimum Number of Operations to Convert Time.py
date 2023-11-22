# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        startH = int(current[:2])
        startM = int(current[-2:])
        endH = int(correct[:2])
        endM = int(correct[-2:])
        if startM > endM:
            endH -= 1
            endM += 60
        return endH - startH + (endM - startM) // 15 + ((endM - startM) % 15) // 5 + (endM - startM) % 5
