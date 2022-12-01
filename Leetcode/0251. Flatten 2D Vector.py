# https://leetcode.com/problems/flatten-2d-vector/

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outerIdx = 0
        self.innerIdx = 0
        if self.outerIdx < len(self.vec) and self.innerIdx >= len(self.vec[self.outerIdx]):
            self.outerIdx += 1
            self.innerIdx = 0
        while self.outerIdx < len(self.vec) and len(self.vec[self.outerIdx]) == 0:
            self.outerIdx += 1

    def next(self) -> int:
        result = self.vec[self.outerIdx][self.innerIdx]
        self.innerIdx += 1
        if self.innerIdx >= len(self.vec[self.outerIdx]):
            self.outerIdx += 1
            self.innerIdx = 0
        while self.outerIdx < len(self.vec) and len(self.vec[self.outerIdx]) == 0:
            self.outerIdx += 1
        return result

    def hasNext(self) -> bool:
        return self.outerIdx < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
