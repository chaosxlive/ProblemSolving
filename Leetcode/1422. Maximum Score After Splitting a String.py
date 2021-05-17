# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        scoreRight = 0
        for c in s:
            if c == '1':
                scoreRight += 1

        scoreMax = 0
        scoreLeft = 0
        for i in range(len(s) - 1):
            if s[i] == '1':
                scoreRight -= 1
            else:
                scoreLeft += 1
            if scoreLeft + scoreRight > scoreMax:
                scoreMax = scoreLeft + scoreRight

        return scoreMax
