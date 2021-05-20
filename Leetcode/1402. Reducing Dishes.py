# https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        afterSum = [0] * len(satisfaction)
        currentSum = satisfaction[0]
        for i in range(len(satisfaction) - 1, 0, -1):
            currentSum += satisfaction[i] * (i + 1)
            afterSum[i - 1] = afterSum[i] + satisfaction[i]
        result = currentSum
        for i in range(len(satisfaction)):
            currentSum -= (afterSum[i] + satisfaction[i])
            if currentSum > result:
                result = currentSum
        return result