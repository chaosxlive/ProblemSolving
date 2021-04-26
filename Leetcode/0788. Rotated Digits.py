# https://leetcode.com/problems/rotated-digits/

class Solution:
    def rotatedDigits(self, N: int) -> int:
        result = 0
        for num in range(2, N + 1):
            isChanged = False
            while num > 0:
                if num % 10 == 3 or num % 10 == 4 or num % 10 == 7:
                    isChanged = False
                    break
                elif num % 10 == 2 or num % 10 == 5 or num % 10 == 6 or num % 10 == 9:
                    isChanged = True
                num //= 10
            if isChanged:
                result += 1

        return result