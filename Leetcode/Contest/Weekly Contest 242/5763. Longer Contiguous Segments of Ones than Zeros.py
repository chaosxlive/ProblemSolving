# https://leetcode.com/contest/weekly-contest-242/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count = 0
        isZero = True
        maxZero = maxOne = 0

        for c in s:
            if isZero:
                if c == '0':
                    count += 1
                else:
                    if count > maxZero:
                        maxZero = count
                    count = 1
                    isZero = False
            else:
                if c == '1':
                    count += 1
                else:
                    if count > maxOne:
                        maxOne = count
                    count = 1
                    isZero = True
        if isZero:
            if count > maxZero:
                maxZero = count
        else:
            if count > maxOne:
                maxOne = count
        return maxOne > maxZero
