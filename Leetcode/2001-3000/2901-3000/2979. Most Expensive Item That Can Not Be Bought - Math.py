# https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        return primeOne * primeTwo - primeOne - primeTwo