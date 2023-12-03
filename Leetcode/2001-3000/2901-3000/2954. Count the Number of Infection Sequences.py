# https://leetcode.com/problems/count-the-number-of-infection-sequences/

from typing import List

MOD = 10**9+7

FACTORIALS = [1] * 100001
for i in range(1, 100001):
    FACTORIALS[i] = (FACTORIALS[i - 1] * i) % MOD

class Solution:
    def numberOfSequence(self, n: int, sicks: List[int]) -> int:
        if len(sicks) == n:
            return 1

        result = 1
        sticks = sicks[0]

        for i in range(1, len(sicks)):
            sickCnt = sicks[i] - sicks[i - 1] - 1
            if sickCnt == 0:
                continue
            result = (result * pow(2, sickCnt - 1, MOD)) % MOD
            result = (result * FACTORIALS[sticks + sickCnt] * pow(FACTORIALS[sticks] * FACTORIALS[sickCnt], MOD - 2, MOD)) % MOD
            sticks += sickCnt
        lastSickCnt = n - sicks[-1] - 1
        if lastSickCnt > 0:
            result = (result * FACTORIALS[sticks + lastSickCnt] * pow(FACTORIALS[sticks] * FACTORIALS[lastSickCnt], MOD - 2, MOD)) % MOD

        return result
