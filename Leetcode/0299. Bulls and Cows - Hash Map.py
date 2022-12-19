# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cntSecret = [0] * 10
        cntGuess = [0] * 10
        a = 0
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                continue
            if cntGuess[int(secret[i])] > 0:
                b += 1
                cntGuess[int(secret[i])] -= 1
            else:
                cntSecret[int(secret[i])] += 1
            if cntSecret[int(guess[i])] > 0:
                b += 1
                cntSecret[int(guess[i])] -= 1
            else:
                cntGuess[int(guess[i])] += 1
        return f"{a}A{b}B"
