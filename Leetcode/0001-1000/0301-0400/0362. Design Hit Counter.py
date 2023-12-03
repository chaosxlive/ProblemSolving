# https://leetcode.com/problems/design-hit-counter/

from bisect import bisect_right


class HitCounter:

    def __init__(self):
        self.times = [-300]
        self.cnts = {}

    def hit(self, timestamp: int) -> None:
        if self.times[-1] != timestamp:
            self.times.append(timestamp)
            self.cnts[timestamp] = 0
        self.cnts[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        i = bisect_right(self.times, timestamp - 300)
        return sum(self.cnts[self.times[j]] for j in range(i, len(self.times)))


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
