# https://leetcode.com/problems/moving-average-from-data-stream/

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.s = size
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.s:
            n = self.q.popleft()
            self.sum -= n
        self.sum += val
        self.q.append(val)
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
