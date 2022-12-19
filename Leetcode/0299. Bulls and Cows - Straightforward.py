# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        used = [[False] * len(secret), [False] * len(secret)]
        a = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                used[0][i] = used[1][i] = True
        b = 0
        for i in range(len(secret)):
            for j in range(len(secret)):
                if used[0][i] or used[1][j]:
                    continue
                if i == j:
                    continue
                if secret[i] == guess[j]:
                    b += 1
                    used[0][i] = used[1][j] = True
        return f"{a}A{b}B"
