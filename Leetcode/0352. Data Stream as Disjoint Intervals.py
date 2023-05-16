# https://leetcode.com/problems/data-stream-as-disjoint-intervals/

from typing import List
from bisect import bisect_left


class SummaryRanges:

    def __init__(self):
        self.container = []

    def addNum(self, value: int) -> None:
        idx = bisect_left(self.container, [value, value])
        if idx > 0 and value <= self.container[idx - 1][1]:
            return
        if idx < len(self.container) and value >= self.container[idx][0]:
            return
        isPrevMerge = idx > 0 and value == self.container[idx - 1][1] + 1
        isNextMerge = idx < len(self.container) and value == self.container[idx][0] - 1
        if isPrevMerge and isNextMerge:
            self.container[idx - 1][1] = self.container[idx][1]
            self.container.pop(idx)
        elif isPrevMerge:
            self.container[idx - 1][1] = value
        elif isNextMerge:
            self.container[idx][0] = value
        else:
            self.container.insert(idx, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.container


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
