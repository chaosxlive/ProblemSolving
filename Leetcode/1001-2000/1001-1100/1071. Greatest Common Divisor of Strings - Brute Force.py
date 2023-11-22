# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        index = 0
        result = ""
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        def checkDivisor(target, divisor):
            if len(target) % len(divisor) != 0:
                return False
            for i in range(len(target)):
                if target[i] != divisor[i % len(divisor)]:
                    return False
            return True

        while index < len(str1) and index < len(str2):
            if str1[index] != str2[index]:
                break
            else:
                pattern = str2[:index + 1]
                if checkDivisor(str1, pattern) and checkDivisor(str2, pattern):
                    result = pattern
            index += 1
        return result
