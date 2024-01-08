# https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        valids = [False] * 100001
        valids[0] = True
        result = 0
        for i in range(1, 100001):
            if (i - primeOne >= 0 and valids[i - primeOne]) or (i - primeTwo >= 0 and valids[i - primeTwo]):
                valids[i] = True
            else:
                result = i
        return result
