# https://leetcode.com/problems/rle-iterator/

from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.rle = encoding
        self.idx = 0
        while self.idx < len(self.rle) and self.rle[self.idx] == 0:
            self.idx += 2

    def next(self, n: int) -> int:
        while self.idx < len(self.rle) and self.rle[self.idx] < n:
            n -= self.rle[self.idx]
            self.idx += 2
        if self.idx >= len(self.rle):
            return -1
        self.rle[self.idx] -= n
        ret = self.rle[self.idx + 1]
        while self.idx < len(self.rle) and self.rle[self.idx] == 0:
            self.idx += 2
        return ret


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
