# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

from math import comb


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = {}

        for domino in dominoes:
            pairs[(min(domino[0], domino[1]), max(domino[0], domino[1]))] = pairs.get((min(domino[0], domino[1]), max(domino[0], domino[1])), 0) + 1

        result = 0
        for n in pairs.values():
            if n >= 2:
                result += comb(n, 2)

        return result
