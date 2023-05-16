# https://leetcode.com/problems/best-team-with-no-conflicts/

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0] * 1001
        result = 0
        for score, age in sorted(zip(scores, ages)):
            dp[age] = score + max(dp[:age + 1])
            result = max(result, dp[age])
        return result
