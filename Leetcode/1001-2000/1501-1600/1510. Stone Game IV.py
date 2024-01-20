# https://leetcode.com/problems/stone-game-iv/

from math import isqrt


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        self.squares = [i * i for i in range(1, isqrt(n) + 1)]
        self.result = [None] * (n + 1)

        def solve(rest):
            if rest == 0:
                self.result[rest] = False
                return False
            if self.result[rest] is not None:
                return self.result[rest]
            self.result[rest] = False
            for sq in self.squares:
                if sq > rest:
                    self.result[rest] = False
                    return False
                result = solve(rest - sq)
                if not result:
                    self.result[rest] = True
                    return True
            self.result[rest] = False
            return False

        solve(n)

        return self.result[n]
