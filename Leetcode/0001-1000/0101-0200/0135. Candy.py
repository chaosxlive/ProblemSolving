# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = 0

        def calcAcc(num):
            return (1 + num) * num // 2

        prevTrend = 0
        left = right = 0
        for index in range(1, len(ratings)):
            currentTrend = 1 if ratings[index] > ratings[index - 1] else (-1 if ratings[index] < ratings[index - 1] else 0)
            if (prevTrend == 1 and currentTrend == 0) or (prevTrend == -1 and currentTrend >= 0):
                result += calcAcc(left) + calcAcc(right) + max(left, right)
                left = 0
                right = 0
            if currentTrend > 0:
                left += 1
            elif currentTrend < 0:
                right += 1
            else:
                result += 1

            prevTrend = currentTrend

        result += calcAcc(left) + calcAcc(right) + max(left, right) + 1
        return result
