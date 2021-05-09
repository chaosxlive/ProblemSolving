# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for col in range(len(word1) + 1)] for row in range(len(word2) + 1)]

        for index2 in range(1, len(word2) + 1):
            for index1 in range(1, len(word1) + 1):
                if word2[index2 - 1] == word1[index1 - 1]:
                    dp[index2][index1] = dp[index2 - 1][index1 - 1] + 1
                else:
                    dp[index2][index1] = max(dp[index2 - 1][index1 - 1], dp[index2 - 1][index1], dp[index2][index1 - 1])
        
        return len(word1) + len(word2) - dp[len(word2)][len(word1)] * 2