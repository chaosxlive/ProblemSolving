# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

class Solution:

    def __init__(self):
        self.dp = [[1, 0] for i in range(31)]
        for i in range(1, 31):
            self.dp[i][0] = self.dp[i - 1][0] + self.dp[i - 1][1]
            self.dp[i][1] = self.dp[i - 1][0]

    def findIntegers(self, n: int) -> int:
        count = 0
        isConsecutived = False
        for i in range(30, -1, -1):
            if n & (1 << i):
                count += self.dp[i][0] + self.dp[i][1]
                if n & (1 << i + 1):
                    isConsecutived = True
                    break

        return count + (0 if isConsecutived else 1)
