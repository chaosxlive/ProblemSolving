# https://leetcode.com/problems/knight-dialer/

MOD = 10**9 + 7


class Solution:
    def __init__(self) -> None:
        self.dp = [[0] * 10 for _ in range(5002)]
        for pos in range(10):
            self.dp[1][pos] = 1
        for step in range(1, 5001):
            for pos in range(10):
                if pos == 1:
                    self.dp[step + 1][6] += self.dp[step][1] % MOD
                    self.dp[step + 1][8] += self.dp[step][1] % MOD
                elif pos == 2:
                    self.dp[step + 1][7] += self.dp[step][2] % MOD
                    self.dp[step + 1][9] += self.dp[step][2] % MOD
                elif pos == 3:
                    self.dp[step + 1][4] += self.dp[step][3] % MOD
                    self.dp[step + 1][8] += self.dp[step][3] % MOD
                elif pos == 4:
                    self.dp[step + 1][3] += self.dp[step][4] % MOD
                    self.dp[step + 1][9] += self.dp[step][4] % MOD
                    self.dp[step + 1][0] += self.dp[step][4] % MOD
                elif pos == 6:
                    self.dp[step + 1][1] += self.dp[step][6] % MOD
                    self.dp[step + 1][7] += self.dp[step][6] % MOD
                    self.dp[step + 1][0] += self.dp[step][6] % MOD
                elif pos == 7:
                    self.dp[step + 1][2] += self.dp[step][7] % MOD
                    self.dp[step + 1][6] += self.dp[step][7] % MOD
                elif pos == 8:
                    self.dp[step + 1][1] += self.dp[step][8] % MOD
                    self.dp[step + 1][3] += self.dp[step][8] % MOD
                elif pos == 9:
                    self.dp[step + 1][2] += self.dp[step][9] % MOD
                    self.dp[step + 1][4] += self.dp[step][9] % MOD
                elif pos == 0:
                    self.dp[step + 1][4] += self.dp[step][0] % MOD
                    self.dp[step + 1][6] += self.dp[step][0] % MOD

    def knightDialer(self, n: int) -> int:
        return 10 if n == 1 else sum(self.dp[n]) % MOD
