# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = [0] * 50

        def getDigitSum(num):
            result = 0
            while num > 0:
                result += num % 10
                num //= 10
            return result

        result = 0
        for n in range(lowLimit, highLimit + 1):
            digitSum = getDigitSum(n)
            box[digitSum] += 1
            result = max(result, box[digitSum])
        return result
