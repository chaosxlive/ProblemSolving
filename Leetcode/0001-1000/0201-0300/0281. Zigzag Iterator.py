# https://leetcode.com/problems/zigzag-iterator/

from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.nums = [0] * (len(v1) + len(v2))
        self.idx = 0
        idxs = [0, 0]
        isV1 = True
        while True:
            if isV1:
                if idxs[0] < len(v1):
                    self.nums[self.idx] = v1[idxs[0]]
                    idxs[0] += 1
                    self.idx += 1
            else:
                if idxs[1] < len(v2):
                    self.nums[self.idx] = v2[idxs[1]]
                    idxs[1] += 1
                    self.idx += 1
            isV1 = not isV1
            if self.idx == len(self.nums):
                break
        self.idx = 0

    def next(self) -> int:
        idx = self.idx
        self.idx += 1
        return self.nums[idx]

    def hasNext(self) -> bool:
        return self.idx < len(self.nums)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
