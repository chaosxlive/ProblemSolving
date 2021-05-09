# https://leetcode.com/problems/super-palindromes/

import math


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        intLeft, intRight = int(left), int(right)
        halfLimit = 100000

        ans = 0

        for n in range(halfLimit):
            tempStr = str(n)
            numSingle = tempStr + tempStr[-2::-1]
            squareSingle = int(numSingle) ** 2
            if squareSingle > intRight:
                break
            if squareSingle >= intLeft and squareSingle == self.intReverse(squareSingle):
                ans += 1

        for n in range(halfLimit):
            tempStr = str(n)
            numDouble = tempStr + tempStr[::-1]
            squareDouble = int(numDouble) ** 2
            if squareDouble > intRight:
                break
            if squareDouble >= intLeft and squareDouble == self.intReverse(squareDouble):
                ans += 1

        return ans

    def intReverse(self, num):
        result = 0
        while num > 0:
            result = 10 * result + num % 10
            num //= 10
        return result
