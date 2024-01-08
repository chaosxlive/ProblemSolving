# https://leetcode.com/problems/super-washing-machines/

from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        L = len(machines)
        avg, mod = divmod(total, L)
        if mod != 0:
            return -1
        diff = 0
        result = 0
        for m in machines:
            diff += m - avg
            result = max(result, m - avg, abs(diff))
        return result
