# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

from typing import List
from functools import lru_cache


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        self.pizza = pizza
        self.k = k

        restApples = [[0] * (len(pizza[0]) + 1) for _ in range(len(pizza) + 1)]
        for r in range(len(pizza) - 1, -1, -1):
            for c in range(len(pizza[0]) - 1, -1, -1):
                restApples[r][c] = sum([
                    restApples[r + 1][c],
                    restApples[r][c + 1],
                    -restApples[r + 1][c + 1],
                    1 if pizza[r][c] == 'A' else 0
                ])

        @lru_cache(None)
        def dfs(row: int, col: int, step: int):
            if restApples[row][col] == 0:
                return 0
            if step == self.k - 1:
                return 1
            result = 0
            for r in range(row + 1, len(pizza)):
                if restApples[row][col] - restApples[r][col] > 0:
                    result = (result + dfs(r, col, step + 1)) % 1000000007
            for c in range(col + 1, len(pizza[0])):
                if restApples[row][col] - restApples[row][c] > 0:
                    result = (result + dfs(row, c, step + 1)) % 1000000007
            return result

        return dfs(0, 0, 0)
