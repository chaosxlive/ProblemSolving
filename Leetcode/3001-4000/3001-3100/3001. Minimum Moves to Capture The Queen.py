# https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if (c + d) % 2 == (e + f) % 2:
            if c + d == e + f:
                return 2 if a + b == e + f and (c < a < e or e < a < c) else 1
            if c - d == e - f:
                return 2 if a - b == e - f and (c < a < e or e < a < c) else 1
        if a == e:
            return 2 if c == e and (b < d < f or f < d < b) else 1
        if b == f:
            return 2 if d == f and (a < c < e or e < c < a) else 1
        return 2
