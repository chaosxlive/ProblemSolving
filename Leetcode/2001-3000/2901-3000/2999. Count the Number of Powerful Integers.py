# https://leetcode.com/problems/count-the-number-of-powerful-integers/

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        def solve(intN: int, strN: str, intS: int, strS: str):
            LN = len(strN)
            LS = len(strS)
            if intN < intS:
                return 0
            if LN == LS:
                return 1
            dp = [[0] * 10 for _ in range(LN)]
            dp[LS][int(strS[0])] = 1
            result = 1
            for i in range(LS + 1, LN):
                for j in range(limit + 1):
                    for k in range(limit + 1):
                        dp[i][j] += dp[i - 1][k]
                    if j > 0:
                        result += dp[i][j]
            for i in range(LN - LS + 1):
                if i == LN - LS:
                    if intN >= int(strN[:-LS]+strS):
                        result += 1
                    break
                for j in range(min(limit + 1, int(strN[i]))):
                    if i == 0 and j == 0:
                        continue
                    for k in range(limit + 1):
                        result += dp[LN - i - 1][k]
                if int(strN[i]) > limit:
                    break
            return result

        resFinish = solve(finish, str(finish), int(s), s)
        resStart = solve(start - 1, str(start - 1), int(s), s)
        return resFinish - resStart
