# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        result = [None] * len(score)
        result[rank[0][0]] = "Gold Medal"
        if len(result) > 1:
            result[rank[1][0]] = "Silver Medal"
        if len(result) > 2:
            result[rank[2][0]] = "Bronze Medal"
        for index in range(3, len(result)):
            result[rank[index][0]] = str(index + 1)
        return result
