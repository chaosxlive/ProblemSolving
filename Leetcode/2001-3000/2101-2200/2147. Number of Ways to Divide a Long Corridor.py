# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        cntS = corridor.count('S')
        if cntS == 0 or cntS % 2 == 1:
            return 0
        parts = corridor.split('S')
        result = 1
        for i in range(2, len(parts) - 2, 2):
            result *= len(parts[i]) + 1
            result %= 10**9+7
        return result
