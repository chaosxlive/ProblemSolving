# https://leetcode.com/problems/edit-distance/

from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]
        for i2, c2 in enumerate(word2):
            for i1, c1 in enumerate(word1):
                if c1 == c2:
                    dp[i2 + 1][i1 + 1] = dp[i2][i1] + 1
                else:
                    dp[i2 + 1][i1 + 1] = max(dp[i2 + 1][i1], dp[i2][i1 + 1])

        @lru_cache
        def dfs(w1, w2, row, col):
            if row == 0:
                return col
            if col == 0:
                return row
            if w1[col - 1] == w2[row - 1]:
                return dfs(w1, w2, row - 1, col - 1)
            result = 2147483647
            if dp[row][col] == dp[row - 1][col - 1]:
                result = min(result, dfs(w1, w2, row - 1, col - 1))
            if dp[row - 1][col] == dp[row][col]:
                result = min(result, dfs(w1, w2, row - 1, col))
            if dp[row][col - 1] == dp[row][col]:
                result = min(result, dfs(w1, w2, row, col - 1))
            return result + 1

        return min(
            dfs(word1, word2, len(word2), len(word1)),
            max(len(word1), len(word2)) - len(list(filter(lambda x: word1[x] == word2[x], [i for i in range(min(len(word1), len(word2)))])))
        )
