# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            isNeg = True
            num *= -1
        else:
            isNeg = False

        result = []
        while num > 0:
            result = [str(num % 7)] + result
            num //= 7
        return "-" + "".join(result) if isNeg else "".join(result)
