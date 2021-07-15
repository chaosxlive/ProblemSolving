# https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[2147483647 for col in range(len(dungeon[0]) + 1)] for row in range(len(dungeon) + 1)]
        dp[-1][-2] = dp[-2][-1] = 1
        for row in range(len(dungeon) - 1, -1, -1):
            for col in range(len(dungeon[0]) - 1, -1, -1):
                dp[row][col] = min(dp[row + 1][col], dp[row][col + 1]) - dungeon[row][col]
                if dp[row][col] <= 0:
                    dp[row][col] = 1
        return dp[0][0]
