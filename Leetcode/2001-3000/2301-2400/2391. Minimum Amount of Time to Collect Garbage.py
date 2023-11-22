# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # M P G
        last0, last1, last2 = -1, -1, -1
        cnts = [[0, 0, 0] for _ in garbage]
        for i, house in enumerate(garbage):
            for c in house:
                if c == 'M':
                    cnts[i][0] += 1
                    last0 = i
                elif c == 'P':
                    cnts[i][1] += 1
                    last1 = i
                else:
                    cnts[i][2] += 1
                    last2 = i
        result = 0
        pos = 0
        while pos < len(garbage):
            result += sum(cnts[pos])
            if pos < last0:
                result += travel[pos]
            if pos < last1:
                result += travel[pos]
            if pos < last2:
                result += travel[pos]
            pos += 1
        return result
