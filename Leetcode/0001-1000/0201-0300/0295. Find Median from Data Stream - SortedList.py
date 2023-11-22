# https://leetcode.com/problems/find-median-from-data-stream/

from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = SortedList()

    def addNum(self, num: int) -> None:
        self.container.add(num)

    def findMedian(self) -> float:
        if len(self.container) % 2 == 0:
            return (self.container[len(self.container) // 2] + self.container[len(self.container) // 2 - 1]) / 2
        return self.container[len(self.container) // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
