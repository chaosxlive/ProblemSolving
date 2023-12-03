# https://leetcode.com/problems/minimum-suffix-flips/

class Solution:
    def minFlips(self, target: str) -> int:
        isZero = True
        cnt = 0
        for c in target:
            if (isZero and c == '1') or (not isZero and c == '0'):
                isZero = not isZero
                cnt += 1
        return cnt
