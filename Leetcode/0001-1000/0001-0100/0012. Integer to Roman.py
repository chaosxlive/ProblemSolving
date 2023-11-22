# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        while num >= 1000:
            result.append("M")
            num -= 1000
        if num >= 900:
            result.append("CM")
            num -= 900
        elif num >= 500:
            result.append("D")
            num -= 500
        elif num >= 400:
            result.append("CD")
            num -= 400
        while num >= 100:
            result.append("C")
            num -= 100
        if num >= 90:
            result.append("XC")
            num -= 90
        elif num >= 50:
            result.append("L")
            num -= 50
        elif num >= 40:
            result.append("XL")
            num -= 40
        while num >= 10:
            result.append("X")
            num -= 10
        if num >= 9:
            result.append("IX")
            num -= 9
        elif num >= 5:
            result.append("V")
            num -= 5
        elif num >= 4:
            result.append("IV")
            num -= 4
        while num >= 1:
            result.append("I")
            num -= 1
        return "".join(result)
