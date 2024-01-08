# https://leetcode.com/problems/magical-string/

class Solution:
    def __init__(self) -> None:
        self.prevOnes = [1, 1, 1]
        self.sResult = [1, 2, 2]
        self.readPtr = 2

    def magicalString(self, n: int) -> int:
        while n > len(self.sResult):
            c = 2 if self.sResult[-1] == 1 else 1
            for _ in range(self.sResult[self.readPtr]):
                self.sResult.append(c)
                self.prevOnes.append(self.prevOnes[-1] + 1 if self.sResult[-1] == 1 else self.prevOnes[-1])
            self.readPtr += 1
        return self.prevOnes[n - 1]
