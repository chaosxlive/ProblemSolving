# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t == 1 and sx == fx and sy == fy:
            return False
        return max(abs(fx - sx), abs(fy - sy)) <= t
