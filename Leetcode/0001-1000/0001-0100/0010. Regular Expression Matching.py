# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        dp = [[False for col in range(lenS + 1)] for row in range(lenP + 1)]

        s += "$"
        p += "$"
        dp[lenP][lenS] = True

        for row in range(lenP - 1, -1, -1):
            for col in range(lenS, -1, -1):
                if p[row] == '*':
                    continue
                                                                                                                                      
                curMatch = (p[row] == s[col] or p[row] == '.') and s[col] != '$'
                if p[row + 1] == '*':
                    if dp[row + 2][col] or (curMatch and dp[row][col + 1]):
                        dp[row][col] = True
                if curMatch and dp[row + 1][col + 1]:
                    dp[row][col] = True

        print(dp)
        return dp[0][0]