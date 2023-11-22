# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def checkNoZero(num):
            while num > 0:
                if num % 10 == 0:
                    return False
                num //= 10
            return True

        for i in range(1, n // 2 + 1):
            if checkNoZero(i) and checkNoZero(n - i):
                return[i, n - i]
        return []

