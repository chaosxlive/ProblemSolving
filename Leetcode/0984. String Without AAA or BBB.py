# https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        count = 0
        isA = a >= b
        while a + b > 0:
            if a >= b and count < 2 or count == 2 and not isA:
                result.append('a')
                a -= 1
                if isA:
                    count += 1
                else:
                    isA = True
                    count = 1
            else:
                result.append('b')
                b -= 1
                if isA:
                    isA = False
                    count = 1
                else:
                    count += 1
        return "".join(result)
