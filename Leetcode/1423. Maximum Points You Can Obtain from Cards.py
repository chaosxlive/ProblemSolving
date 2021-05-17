# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        discardCount, discardSum = len(cardPoints) - k, 0

        for i in range(discardCount):
            discardSum += cardPoints[i]
        discardMinSum = totalSum = discardSum

        for i in range(discardCount, len(cardPoints)):
            totalSum += cardPoints[i]
            discardSum += cardPoints[i] - cardPoints[i - discardCount]
            if discardSum < discardMinSum:
                discardMinSum = discardSum

        return totalSum - discardMinSum
