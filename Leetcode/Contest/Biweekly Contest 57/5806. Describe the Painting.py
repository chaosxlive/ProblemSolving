# https://leetcode.com/contest/biweekly-contest-57/problems/describe-the-painting/

from sortedcontainers import SortedDict


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        values = SortedDict()
        for start, end, val in segments:
            values[start] = values.get(start, 0) + val
            values[end] = values.get(end, 0) - val

        result = []
        items = values.items()
        current = items[0][1]
        for i in range(1, len(items)):
            if current:
                result.append([items[i - 1][0], items[i][0], current])
            current += items[i][1]
        return result
