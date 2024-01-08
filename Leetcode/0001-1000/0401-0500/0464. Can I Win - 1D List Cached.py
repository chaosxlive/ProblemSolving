# https://leetcode.com/problems/can-i-win/


class Solution:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        self.cache = [0] * (2**(maxChoosableInteger + 1) + 1)

        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 == desiredTotal:
            return maxChoosableInteger % 2 == 1
        if desiredTotal <= 0:
            return True

        def solve(chosen: int, rest: int):
            if self.cache[chosen] != 0:
                return self.cache[chosen] == 1
            if rest <= 0:
                self.cache[chosen] = -1
                return False
            for i in range(1, maxChoosableInteger + 1):
                mask = 1 << i
                if chosen & mask:
                    continue
                if not solve(chosen | mask, rest - i):
                    self.cache[chosen] = 1
                    return True
            self.cache[chosen] = -1
            return False

        return solve(0, desiredTotal)
