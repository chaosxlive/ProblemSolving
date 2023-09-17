# https://leetcode.com/problems/furthest-point-from-origin/

from collections import Counter


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = Counter(moves)
        return max(c['L'], c['R']) - min(c['L'], c['R']) + c['_']
