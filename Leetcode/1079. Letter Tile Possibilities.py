# https://leetcode.com/problems/letter-tile-possibilities/

from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return sum(len(set(permutations(tiles, l))) for l in range(1, len(tiles) + 1))
